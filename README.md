# second-brain-with-db2

> A working second brain you actually build yourself — with IBM Db2 as the foundation and AI doing the heavy lifting.

## Vision

Most "second brain" tools are products you subscribe to. You feed them your articles, notes, and PDFs, and trust a black box to organize and surface what matters.

This repository takes a different path: it's a **build-it-yourself second brain**, and the database underneath isn't a hidden vector store you'll never see. It's IBM Db2 — the same enterprise database that runs banks, airlines, and supply chains — used here to power a personal AI application.

The point isn't just to end up with a working knowledge base. It's to show, step by step and at the code level, what it actually takes to build an AI-native application on Db2: storing documents, generating embeddings, running vector search, integrating with LLMs, and orchestrating the whole pipeline. By the end you'll have your own second brain *and* a clear mental model for building similar AI applications on Db2 for any domain.

This is a teaching repository disguised as a personal tool. Every stage is small enough to read in one sitting, runnable on its own, and progressive — Stage 1 is fifty lines of Python; later stages add Db2 storage, vector embeddings, LLM-powered summarization and categorization, and retrieval-augmented Q&A.

If you're an application developer who wants to understand how to use Db2 as the infrastructure for real AI applications, this is for you. If you're a knowledge worker who's tired of letting opaque SaaS tools own your reading and thinking, this is also for you.

## The Use Case

I'm an AI architect for IBM Db2. Every week I come across articles, blog posts, research papers, technical documentation, PDFs, and conference talks worth coming back to. Saving them in cloud folders or browser bookmarks is where good intentions go to die — once something is "saved," I rarely find it again.

What I actually want is a place where my reading material lives, gets understood, and stays useful:

- **Capture from anywhere.** Paste a URL. Upload a PDF. Drop in a document. The app fetches the content, extracts the meaningful text (no ads, no navigation chrome), and stores it.
- **Understand on arrival.** Each item is summarized and tagged automatically by an LLM — so a 40-page paper or a long-read article gives me its argument in five sentences without me re-reading it.
- **Categorize and connect.** Across everything I've collected, the app finds themes: what topics are recurring, what sources are converging on the same ideas, what's actually fresh versus rehashed.
- **Search by meaning, not keywords.** Vector search over the full text means I can ask *"what did anyone say about hybrid retrieval in production?"* and get answers from a six-month-old blog post and a paper from last week, with citations.
- **Synthesize on demand.** Ask the second brain a real question and it answers using only the material I've collected — grounded in my own curated reading, not the open internet.

Db2 is the foundation throughout. The full text, the metadata, the vector embeddings, the tags, the relationships between items — all stored and queried in Db2. The same SQL that runs the world's enterprise data also runs my second brain. That's the demonstration.

## How the repository is organized

This is a staged build. Each stage stands alone, runs end-to-end, and adds one new capability. You can follow along chapter by chapter, or jump to the stage that solves your problem.

*Stages and detailed walkthroughs will appear here as the repository grows.*
