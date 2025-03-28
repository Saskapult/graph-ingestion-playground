# Knowledge Graph Generator for Cedar 
Creates a knowledge graph using [kg-gen](https://github.com/stair-lab/kg-gen) using the phi-4 LLM hosted on ollama on the Cedar compute cluster. 


## Usage 
- Run `bash build_container_job.sh` to build the apptainer
	- This will take a long time
	- If it throws errors just run it again
- Run `bash get_data.sh` to fetch the data 
- Run `sbatch ingestion_job.sh fema_nims_doctrine-2017.pdf ./output`
	- This currently only processes the first three documents and throws an error for the third one (fix incoming shortly)
- Tun `sq` a bunch of times to know when it's done 
- Look in `./output` for results. 


## The Documentation
The part where I explain how it works. 


### The Apptainer 
An apptainer is used for several reasons:
- Provides a consistent running environment 
- Provides a fake root environment 
- Includes model data so we don't need to waste allocated time to download it again 

The apptainer build script does a lot of things. Most of them are elaborated on in the build script itself. 
It was an incredible pain to develop. 

>[!warning] Build Duration
>
>Do not build this on Arbutus. A basic version took 40 minutes to build each time. Each time! Building it on Cedar is better, taking only 15 minutes to build.

>[!warning] Allocation Error
>
>Sometimes there is an allocation error while building the container. I do not know why. Just run it again. 

>[!warning] Port in use
>
>Sometimes an apptainer process decides to rebel and keep running. I do not know why. Just log out of Cedar or hunt it down and kill it on Arbutus (use `sudo ss --tcp --listening --processes 'sport = 11434'`).

The apptainer can be run as a daemon or as a regular runnable apptainer. 
In either case it starts the ollama server in the background. 

While the python scripts live outside of the apptainer, their dependencies (specified in `pyproject.toml` and `uv.lock`) are frozen within the apptainer. 
One can modify the scripts without rebuilding the apptainer but any dependency edits require a rebuild of the container. 
I've chosen to not include the python environment/scripts in this because it is far easier for testing and usage in other applications. 
It could be worth experimenting with in the future but I wouldn't be convinced it's a good idea without good profiling data. 


### The Job 
The job requests that a [signal](https://services.criann.fr/en/services/hpc/cluster-myria/guide/signals-sent-by-slurm/) be sent in notification to the depletion of its allotted time. 
This is currently unused, but I'm sure you can think of applications for it. 

The apptainer is copied to node-local storage to improve repeated access performance. 
The scripts and input file are left on network storage because they are small and I'm not convinced it's necessary to move them. 

TODO: Work resubmission upon cancellation 


### The Script 

The input document is split into chunks, each of which is turned into a small knowledge graph. 
These small chunks are saved as checkpoints. 
If an existing checkpoint for a chunk is detected, its processing will be skipped. 
This allows us to perform work incrementally, allowing the program to be cancelled and then resume its work. 
