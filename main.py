from kg_gen import KGGen, Graph
import graph
import pdf
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	parser.add_argument("-o", "--output")
	# parser.add_argument("-m", "--model", default="")
	args = parser.parse_args()

	print(f"Reading {args.filename}")
	print(f"Outputting to {args.output}")

	print("Hello from graph-ingestion-playground!")

	pages = pdf.get_pdf_pages_text(args.filename)
	# TODO: Make it smarter 
	# Maybe aggregate text until a threshold is reached, then attach sources to that 
	# Not sure how to split it though, by sentences or words or characters? 
	chunks = pdf.make_pdf_chunks(pages)
	
	# print("First three chunks")
	# for c in chunks[:3]:
	# 	print("--")
	# 	print(c)
	# print("--")

	kg = KGGen(
		model=kg_gen_model,
		api_key=os.getenv("OPENAI_API_KEY"),
	)

	for i, entry in enumerate(chunks):
		print(f"Process chunk {i+1}/{len(chunks)}")
		graph = kg.generate(
			input_data=entry,
		)

		graph_json = graph.graph_to_json(graph)
		file = args.output + f"/chunk-{i}.json"
		print(f"\tSaving as '{file}'")
		graph.save_json(graph_json, file)


if __name__ == "__main__":
	main()
