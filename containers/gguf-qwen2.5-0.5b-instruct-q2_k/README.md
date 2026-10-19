# `gguf-qwen2.5-0.5b-instruct-q2_k`
A `scratch` image containing a single GGUF model file, [Qwen2.5-0.5B-Instruct Q2_K](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF),
at `/models/qwen2.5-0.5b-instruct-q2_k.gguf` (415,182,688 bytes).

The model's tensor data extends well past the first 50 MB of the file. syft only parses the first 50 MB of a GGUF file, so this image
covers models whose tensor data doesn't fit in that window (ENTERPRISE-9708). Analysis should produce a single `model` package named
`qwen2.5-0.5b-instruct`.

The download is pinned to a Hugging Face repo commit and verified against the file's sha256.
