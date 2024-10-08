import marimo

__generated_with = "0.9.3"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell
def __(mo):
    llm_model = mo.ui.dropdown(options=['llama3.2','llama3.1','qwen2.5'], label="Choose LLM model", value="llama3.1")

    base_url = mo.ui.dropdown(options={'localhost':'http://localhost:11434', 
                                       '10.127.127.2':'http://10.127.127.2:11434',
                                       '10.127.127.5':'http://10.127.127.5:11434',
                                      },
                              label="Choose Ollama base_url",
                              value='localhost'
                             )

    temperature = mo.ui.slider(0,1,0.1, label='temperature')
    return base_url, llm_model, temperature


@app.cell
def __(base_url, llm_model, mo, temperature):
    horizontal = mo.hstack(
                           items=[llm_model,
                                   base_url,
                                   temperature],
                            justify="space-around",
                            gap=0.5

                          )
    return (horizontal,)


@app.cell
def __(horizontal):
    horizontal
    return


@app.cell
def __(llm_model):
    llm_model
    return


@app.cell
def __(temperature):
    temperature
    return


@app.cell
def __(base_url):
    base_url
    return


@app.cell
def __():
    return


@app.cell
def __(base_url, llm_model, temperature):
    from langchain_ollama import ChatOllama

    llm = ChatOllama(
        model = llm_model.value,
        temperature = temperature.value, 
        base_url = base_url.value
    )
    return ChatOllama, llm


@app.cell
def __(llm):
    # json_llm = ChatOllama(format="json")
    messages = [
         ("system", "You are a helpful translator. Translate the user sentence to French."),
        ("human", "I love programming."),
    ]
    llm.invoke(messages)
    return (messages,)


@app.cell
def __(ChatOllama, base_url, llm_model, temperature):
    json_llm = ChatOllama(
                format="json",
                model = llm_model.value,
                temperature = temperature.value, 
                base_url = base_url.value
    )
    return (json_llm,)


@app.cell
def __(json_llm):
    messages2 = [
        ("human", "Return a query for the weather in a random location and time of day with two keys: location and time_of_day. Respond using JSON only."),
    ]
    json_llm.invoke(messages2).content
    return (messages2,)


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
