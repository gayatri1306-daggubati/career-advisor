import google.generativeai as genai
genai.configure(api_key="AIzaSyAXy1hretw9bWBAf87GSwrN6-hsEhyCn54")

models = genai.list_models()
for m in models:
    print(m.name)
