# OpenAssistantAPISetup

```git clone https://github.com/mitscheltobi/OpenAssistantAPISetup```

### Prerequisites
You need to run the inferenceSetup on Ubuntu (specifically to set up docker).
Also make sure to make the script executable ```sudo chmod +x inferenceSetup.sh``` and run it with priviledges ```sudo inferenceSetup.sh```


### Steps
- First run the API setup script (inferenceSetup.sh): This will download the model and set up an API using the huggingface text generation interface ([text-generation-inference](https://github.com/huggingface/text-generation-inference))
- Upon successfull loading of the model and setting up the inference endpoint, you can then use the testAPI.py script to test the endpoint. You can pass a prompt as a command line argument, without having to enter any special tokens.

You can also reach the API on localhost on port 8080 using the endpoints generate and generate_stream ([more information here](https://github.com/huggingface/text-generation-inference#docker))
