# Knowledge Graph Generator for Cedar 

## Usage 
- Run `bash build_container_job.sh` to build the apptainer
	- This will take a long time
- Run `bash get_data.sh` to fetch the data 
- Run `sbatch ingestion_job.sh`
	- This currently only processes the first three documents and throws an error for the third one (fix incoming shortly)
- Tun `sq` a bunch of times to know when it's done 
- Look in `/home/<your account>/scratch/<time of submission>` for results. 
