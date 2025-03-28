from kg_gen import KGGen, Graph
import graph
import pdf
import argparse
import os


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	parser.add_argument("-o", "--output")
	# parser.add_argument("-m", "--model", default="")
	parser.add_argument("--only", default="")
	args = parser.parse_args()

	print(f"Reading {args.filename}")
	print(f"Outputting to {args.output}")

	print("Hello from graph-ingestion-playground!")

	pages = pdf.get_pdf_pages_text(args.filename)
	# TODO: Make it smarter 
	# Maybe aggregate text until a threshold is reached, then attach sources to that 
	# Not sure how to split it though, by sentences or words or characters? 
	chunks = pdf.make_chunks(pages)
	
	# print("First three chunks")
	# for c in chunks[:3]:
	# 	print("--")
	# 	print(c)
	# print("--")

	print("Connecting to model")
	kg = KGGen(
		model="ollama/phi4",
	)

	for i, (entry, (st, en)) in enumerate(chunks):
		# Early termination option for testing
		if args.only != "" and args.only.isdigit() and int(args.only) <= i:
			print(f"Stopping after first {args.only} chunks")
			break

		print(f"Process chunk {i+1}/{len(chunks)}")

		# Check for checkpoint
		chunk_output_path = args.output + f"/chunk-{i}-{st}-{en}.json"
		if os.path.isfile(chunk_output_path):
			print("\tSkipping due to checkpoint detection!")
			continue
		
		kgraph = kg.generate(
			input_data=entry,
		)
		
		print(f"\tSaving as '{chunk_output_path}'")
		graph_json = graph.graph_to_json(kgraph)
		graph.save_json(graph_json, chunk_output_path)
	
	print(f"All chunks processed, output is in {args.output}")


if __name__ == "__main__":
	main()
