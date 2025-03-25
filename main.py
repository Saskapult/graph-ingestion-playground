from kg_gen import KGGen, Graph
import graph
import pdf
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("filename")
	parser.add_argument("-o", "--output")
	args = parser.parse_args()

	print(f"Reading {args.filename}")
	print(f"Outputting to {args.output}")

	print("Hello from graph-ingestion-playground!")

	# pages = pdf.get_pdf_pages_text(args.filename)
	# chunks = pdf.make_pdf_chunks(pages)
	
	# print("First three chunks")
	# for c in chunks[:3]:
	# 	print("--")
	# 	print(c)
	# print("--")

	# for i, entry in enumerate(chunks):
	# 	print(f"Process chunk {i+1}/{len(chunks)}")
	# 	graph = None

	# 	sources = entry["sources"]
	# 	graph_json = graph.graph_to_json(graph)

	# 	file = args.output + f"/chunk-{sources}.json"
	# 	print(f"\tSaving as '{file}'")
	# 	graph.save_json(graph_json, file)
		

	# We get all of the entities and relation and we link them to this page

	# A node is just an id 
	# A relationship has a source (pdf page number)
	# Relationship RELATION has [edge, page number]
	
	# 
	# When answering 
	# 
	# Create KG 
	# Find similar items in db 
	# expand idk 
	# 
	# Have lsit of relations 
	# 
	# Get relations
	# Find 
	# I need to read a paper on this 
	# 

	# kg = KGGen(
	# 	model=kg_gen_model,
	# 	api_key=os.getenv("OPENAI_API_KEY"),
	# )
	# graph = kg.generate(
	# 	input_data=entry["html"],
	# 	output_folder="./scratch"
	# )


if __name__ == "__main__":
	main()
