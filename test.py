import pinecone

# Initialize Pinecone with just the API key
pinecone.init(api_key='b1d78acd-4331-4743-9967-8bcf0e8eb197')

# Print the list of environments
print("Available Pinecone Environments:")
for env in pinecone.list_indexes():
    print(env)