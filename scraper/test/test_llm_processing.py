from .. import llm_processing


def test_openai_completion():
    prompt = (
        "Your job is to write a 3 sentence story about the topic provided by the user."
    )
    input = "Theo Walcott"

    output = llm_processing.openai_completion(prompt, input)
    assert type(output) == str
    assert len(output) > 0
