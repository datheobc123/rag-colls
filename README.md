# rag-colls

**rag-colls** a.k.a **RAG Coll**ection**s**.

Simple and easy to use, production-ready advanced RAG techniques.

<div align="center">

![Downloads](https://img.shields.io/pypi/dm/rag_colls)  ![License](https://img.shields.io/badge/license-MIT-green)

![GitHub CI](https://github.com/hienhayho/rag-colls/actions/workflows/docker-build.yml/badge.svg) ![GitHub CI](https://github.com/hienhayho/rag-colls/actions/workflows/installation-testing.yml/badge.svg)

</div>

## 📖 Documentation

Please visit [documentation](https://rag-colls.readthedocs.io/en/latest/) to get latest update.

## 🔧 Installation

- You can easily install it from **pypi**:

```bash
pip install -U rag-colls
```

- **Docker** - 🐳:

```bash
# Clone the repository
git clone https://github.com/hienhayho/rag-colls.git
cd rag-colls/

# Docker build
DOCKER_BUILDKIT=1 docker build -f docker/Dockerfile \
                    --build-arg OPENAI_API_KEY=<YOUR_OPENAI_KEY> \
                    --build-arg PYTHON_VERSION="3.10" \
                    -t rag-colls:3.10 .
```

## 📚 Notebooks

We have provided some notebooks for example usage.

| RAG Tech | Code | Guide | Tech Description |
|:----------:|:----------:|:----------:|:----------:|
| BasicRAG | [BasicRAG](./rag_colls/rags/basic_rag) | [Colab](https://colab.research.google.com/drive/19hzGSQqx-LIsSbnNkV71ipRAIiFingvP)| Integrate with [`Chromadb`](rag_colls/databases/vector_databases/chromadb.py) |
| ContextualRAG |[ContextualRAG](rag_colls/rags/contextual_rag)| [Colab](https://colab.research.google.com/drive/1vT2Wl8FzYt25_4CMMg-2vcF4y17iTSjO) | Integrate with [`Chromadb`](rag_colls/databases/vector_databases/chromadb.py) and [`BM25s`](rag_colls/databases/bm25/bm25s.py) version |

## 🚀 Upcoming

We are currently working on these projects and will be updated soon.

| RAG Tech | Link |
|:----------:|:----------:|
| RAFT | [Blog](https://techcommunity.microsoft.com/blog/aiplatformblog/raft-a-new-way-to-teach-llms-to-be-better-at-rag/4084674), [Paper](https://arxiv.org/pdf/2403.10131)|
| RAG-RL |[Paper](https://arxiv.org/pdf/2503.12759)|

## 🎉 Quickstart

Please refer to [example](./examples) for more information.

## 💻 Develope Guidance

Please refer to [DEVELOP.md](./DEVELOP.md) for more information.

## ✨ Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 75.0; height: 75.0">
        <a href=https://github.com/hienhayho>
            <img src=https://avatars.githubusercontent.com/u/115549171?v=4 width="50;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Ho Trong Hien/>
            <br />
            <sub style="font-size:10px"><b>Ho Trong Hien</b></sub>
        </a>
    </td>
</tr>
</table>

## ©️ LICENSE

`rag-colls` is under [MIT LICENSE.](./LICENSE)
