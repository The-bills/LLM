import tiktoken


def count_tokens(prompt, encoding_name="cl100k_base") -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(prompt))
    return num_tokens


"""
Koszt embeddingu + koszt query
"""
