# OpenAssistantAPISetup

```git clone https://github.com/mitscheltobi/OpenAssistantAPISetup```


### Steps
- First run the API setup script (inferenceSetup.sh): This will download the model and set up an API using the huggingface text generation interface ([huggingface /](https://github.com/huggingface/text-generation-inference))
- Upon successfull loading of the model and setting up the inference endpoint, you can then use the testAPI.py script to test the endpoint. You can pass a prompt as a command line argument, without having to enter any special tokens.

You can also reach the API on localhost on port 8080 using the endpoints generate and generate_stream ([huggingface /] https://github.com/huggingface/text-generation-inference#docker)
