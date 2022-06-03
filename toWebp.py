import tinify

tinify.key = "vMsNmcZQljq5RN9RfxSsJwsbW0LXrnkl"

source = tinify.from_file("to_1.0.png")
source.to_file("to_1.0.webp")