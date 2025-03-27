#SBATCH --time=00:1:00
#SBATCH --account=def-ycoady

echo "Hello"
ls > scratch/test_output_ls
echo "world"
uv sync > scratch/test_output_uv
echo "!"

exit 0
