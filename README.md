# 🐾 WildGPT

## 🌿 Overview

WildGPT is an AI-based chatbot application 🤖 designed to scrape and consolidate publicly available research papers and data related to wildlife, biodiversity, and conservation. 🌱🦅

It uses various libraries and tools 📚 to extract, ingest, and split documents, and then creates a retriever and chain for further processing. It’s a highly maintainable Python-based Generative AI project 🐍⚡ that processes and analyzes PDF documents and web-scraped content.

We designed a cost-effective bot 💸 to scrape online data from web pages 🌐. The process of opening web pages and extracting data is automated. Our custom open-source Ollama model 📊 generates rich information on wildlife, biodiversity, and conservation using the gathered knowledge base.

### 👥 Authors
- 🧑‍💻 Mrinal Raj
- 🧑‍💻 Dhananjaya G R
- 🧑‍💻 Sri Sai Pamu
- 🧑‍💻 Shrish Jain

### 📦 Dependencies
- 🌐 Google Chrome
- 🐍 Anaconda
- 🧠 Ollama Engine

### ⚙️ Constants
- EMBEDDING_MODEL: ‘nomic-embed-text’
- VECTOR_STORE_NAME: ‘simple_rag’
- MODEL: ‘llama3.1’
- DOC_FOLDER: Path to the folder containing PDF documents 📚
- RES_FOLDER: Path to the folder containing resources that are available locally 📁
 

## 🚀 Deployment

### 🛠️ Creating Virtual Environment
```
conda --version
conda init
conda create -n <new_venv_name> python=3.12
conda env list
source /opt/homebrew/Caskroom/miniconda/base/etc/profile.d/conda.sh
conda activate <new_venv_name>
pip install -r requirement.txt
```

### 🔥 Running Ollama Engine (Terminal 1)
```
ollama serve
```
You should see something like this when deployment is successful ✅:
```sh
2025/03/21 08:48:44 routes.go:1230: INFO server config env="map[HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:2048 OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:/Users/dguntira/.ollama/models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false http_proxy: https_proxy: no_proxy:]"
time=2025-03-21T08:48:44.061+05:30 level=INFO source=images.go:432 msg="total blobs: 20"
time=2025-03-21T08:48:44.061+05:30 level=INFO source=images.go:439 msg="total unused blobs removed: 0"
time=2025-03-21T08:48:44.062+05:30 level=INFO source=routes.go:1297 msg="Listening on 127.0.0.1:11434 (version 0.6.2)"
time=2025-03-21T08:48:44.115+05:30 level=INFO source=types.go:130 msg="inference compute" id=0 library=metal variant="" compute="" driver=0.0 name="" total="10.7 GiB" available="10.7 GiB"
[GIN] 2025/03/21 - 08:52:32 | 200 |    1.3560275s |       127.0.0.1 | POST     "/api/pull"
time=2025-03-21T08:52:33.122+05:30 level=WARN source=types.go:522 msg="invalid option provided" option=tfs_z
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.vision.block_count default=0
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.head_count_kv default=1
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.key_length default=64
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.value_length default=64
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.head_count_kv default=1
time=2025-03-21T08:52:33.127+05:30 level=INFO source=sched.go:715 msg="new model will fit in available VRAM in single GPU, loading" model=/Users/dguntira/.ollama/models/blobs/sha256-970aa74c0a90ef7482477cf803618e776e173c007bf957f635f1015bfcfef0e6 gpu=0 parallel=1 available=11453251584 required="864.9 MiB"
time=2025-03-21T08:52:33.127+05:30 level=INFO source=server.go:105 msg="system memory" total="16.0 GiB" free="5.3 GiB" free_swap="0 B"
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.vision.block_count default=0
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.head_count_kv default=1
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.key_length default=64
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.value_length default=64
time=2025-03-21T08:52:33.127+05:30 level=WARN source=ggml.go:149 msg="key not found" key=nomic-bert.attention.head_count_kv default=1
time=2025-03-21T08:52:33.127+05:30 level=INFO source=server.go:138 msg=offload library=metal layers.requested=-1 layers.model=13 layers.offload=13 layers.split="" memory.available="[10.7 GiB]" memory.gpu_overhead="0 B" memory.required.full="864.9 MiB" memory.required.partial="864.9 MiB" memory.required.kv="24.0 MiB" memory.required.allocations="[864.9 MiB]" memory.weights.total="216.1 MiB" memory.weights.repeating="216.1 MiB" memory.weights.nonrepeating="44.7 MiB" memory.graph.full="48.0 MiB" memory.graph.partial="48.0 MiB"
llama_model_load_from_file_impl: using device Metal (Apple M2 Pro) - 10922 MiB free
llama_model_loader: loaded meta data with 24 key-value pairs and 112 tensors from /Users/dguntira/.ollama/models/blobs/sha256-970aa74c0a90ef7482477cf803618e776e173c007bf957f635f1015bfcfef0e6 (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = nomic-bert
llama_model_loader: - kv   1:                               general.name str              = nomic-embed-text-v1.5
llama_model_loader: - kv   2:                     nomic-bert.block_count u32              = 12
llama_model_loader: - kv   3:                  nomic-bert.context_length u32              = 2048
llama_model_loader: - kv   4:                nomic-bert.embedding_length u32              = 768
llama_model_loader: - kv   5:             nomic-bert.feed_forward_length u32              = 3072
llama_model_loader: - kv   6:            nomic-bert.attention.head_count u32              = 12
llama_model_loader: - kv   7:    nomic-bert.attention.layer_norm_epsilon f32              = 0.000000
llama_model_loader: - kv   8:                          general.file_type u32              = 1
llama_model_loader: - kv   9:                nomic-bert.attention.causal bool             = false
llama_model_loader: - kv  10:                    nomic-bert.pooling_type u32              = 1
llama_model_loader: - kv  11:                  nomic-bert.rope.freq_base f32              = 1000.000000
llama_model_loader: - kv  12:            tokenizer.ggml.token_type_count u32              = 2
llama_model_loader: - kv  13:                tokenizer.ggml.bos_token_id u32              = 101
llama_model_loader: - kv  14:                tokenizer.ggml.eos_token_id u32              = 102
llama_model_loader: - kv  15:                       tokenizer.ggml.model str              = bert
llama_model_loader: - kv  16:                      tokenizer.ggml.tokens arr[str,30522]   = ["[PAD]", "[unused0]", "[unused1]", "...
llama_model_loader: - kv  17:                      tokenizer.ggml.scores arr[f32,30522]   = [-1000.000000, -1000.000000, -1000.00...
llama_model_loader: - kv  18:                  tokenizer.ggml.token_type arr[i32,30522]   = [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...
llama_model_loader: - kv  19:            tokenizer.ggml.unknown_token_id u32              = 100
llama_model_loader: - kv  20:          tokenizer.ggml.seperator_token_id u32              = 102
llama_model_loader: - kv  21:            tokenizer.ggml.padding_token_id u32              = 0
llama_model_loader: - kv  22:                tokenizer.ggml.cls_token_id u32              = 101
llama_model_loader: - kv  23:               tokenizer.ggml.mask_token_id u32              = 103
llama_model_loader: - type  f32:   51 tensors
llama_model_loader: - type  f16:   61 tensors
```

### 🧩 Running Backend Server (Terminal 2)
```
python /<your_absolute_path_from_root>/wildgpt/app.py
```
You should be able to see something like below -
Wait for Debugger PIN: to be available (That's when your backend is completly ready)
```sh
 * Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 328-018-644
Backend Available on http://127.0.0.1:8000/chat for REST calls
```

### 🌐 Running Frontend Server (Terminal 3)
```
cd /<your_absolute_path_from_root>/wildgpt/frontend/
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
export NVM_DIR="$HOME/.nvmn["\n[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm\n[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
npm install 20
npm use 20
npm run dev
```
Open the frontend in Google Chrome 🌐 by using Local or Network socket:
```sh

> wildlife-chatbot-frontend@0.0.0 dev
> vite


  VITE v5.4.0  ready in 347 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
Browserslist: caniuse-lite is outdated. Please run:
  npx update-browserslist-db@latest
  Why you should do it regularly: https://github.com/browserslist/update-db#readme
```
 
### 💬 Running WildGPT Chatbot Shell Version (Terminal 4) - Optional
```
python /<your_absolute_path_from_root>/wildgpt/wildpgt_chatbot.py
```
When successful, you’ll see:
```sh
 Hey there !!
    I'm WildGPT, an AI-powered tool designed to scrape and consolidate publicly available research papers and data related to wildlife, biodiversity, and conservation.
    Ask me anything about the latest research trends.

    If you want to end conversation, type 'exit' or 'quit' or 'end'

========================================================================================================================================================================================================

[User's query]: >>> 
```

### 🐞 Debugging if Something Isn’t as Expected

#### 🧠 For Ollama Engine
```sh
(mrinal_env) (base) mriraj@wildgpt % ollama list
NAME                                                 ID              SIZE      MODIFIED     
nomic-embed-text:latest                              0a109f422b47    274 MB    3 hours ago     
WildGPT:latest                                       5355ef75aa0b    4.9 GB    37 hours ago    
llama3.1:latest                                      46e0c10c039e    4.9 GB    37 hours ago    
(mrinal_env) (base) mriraj@wildgpt % 
```
#### 🖥️ For Backend Server
```
- Method: POST
- URL: http://localhost:8000/chats
- Headers: Content-Type: application/json
- Body: {"message": "<your_query_here>"}
- Response: The function returns a promise that resolves to the JSON data from the response if the request is successful. If the request fails, it rejects the promise with an object containing the status code and the response data.
```

### 🧹 Decommissioning: Disabling & Deleting venv

#### ⛔ Stopping Running Services
Use Ctrl + C to stop:
- 🐚 Shell version of WildGPT (if running)
- 🌐 Frontend Server
- ⚙️ Backend Server
- 🧠 Ollama Engine

#### 🧼 Deactivating & Deleting Virtual Environment
```
conda deactivate
conda env remove -n<new_venv_name>
```
