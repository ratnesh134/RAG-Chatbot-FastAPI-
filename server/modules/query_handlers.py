from logger import logger



def query_chain(chain,user_input:str):

    try :
        logger.debug(f"Running chain for input: {user_input}")
        result = chain({"query" : user_input})
        responses = {
            "response" : result["result"],
            "sources" : [doc.metadata.get("source","") for doc in result["source_documents"]]

        }
        logger.debug(f"Chain response : {responses}")
        return responses
    
    except Exception as e:
        logger.exception("Error in query_chain")
        raise
     
