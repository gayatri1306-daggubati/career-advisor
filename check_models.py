<<<<<<< HEAD
import google.generativeai as genai
genai.configure(api_key="AIzaSyAXy1hretw9bWBAf87GSwrN6-hsEhyCn54")

models = genai.list_models()
for m in models:
    print(m.name)
=======
import google.generativeai as genai
genai.configure(api_key="AIzaSyAXy1hretw9bWBAf87GSwrN6-hsEhyCn54")

models = genai.list_models()
for m in models:
    print(m.name)
>>>>>>> db06363a0da4f63e1601dc714478633b7316e50e
