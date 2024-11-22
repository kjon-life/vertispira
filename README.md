

# Hello! [WIP]

I've been a builder 🍀 all my life making systems that work for enterprise, production loads. I am an `avocational` product manager, because enterprise "products" _are_ **the systems we build** to solve problems.

It's a subtle, distinct difference: Individuals buy products, enterprise buys solutions. 

Everything we build has far-reaching effects. None more so than `AI agents` or `bots` or whatever the common vocabulary will come to call them. Not only the technology, but the ways in which we interact with them.

The current plateau in LLM improvements seems to be stimulating interest in ways LLMs enable agentic workflows...the systems by which `AI systems` research, revise, improve.  The current vertex is one in which multiple agents collaborate--are collaborating--to create autonomous solutions.

This project is an exploration of evals applied to agentic workflows. Applying modular development patterns to the most rapidly evolving field in history.

<img align="right" width="300" src="https://user-images.githubusercontent.com/76539355/214731371-78cb7bcb-996d-4108-9872-7af758ed5647.png" alt="A Maia">



## 🌀  &middot; Rua Vertex   
[![Fly Deploy](https://github.com/kjon-life/kjon-life/actions/workflows/fly.yml/badge.svg)](https://github.com/kjon-life/kjon-life/actions/workflows/fly.yml) 
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/kjon-life/kjon-life) 
 ![GitHub License](https://img.shields.io/github/license/kjon-life/kjon-life)
 ![GitHub top language](https://img.shields.io/github/languages/top/kjon-life/kjon-life)
 ![W3C Validation](https://img.shields.io/w3c-validation/html?targetUrl=https%3A%2F%2Fkjon.life) 
 
This is a project that feeds my developer portfoio. To connect:  
- Mention me in an issue or pull request: @kjon-life  
- My friends connect on [Instagram: @kilo.jon](https://www.instagram.com/kilo.jon/)   
- [LinkedIn](https://www.linkedin.com/in/jonhwilliams) for professional connections.

### About:  
- I work in the intersections of programming, performance, and revenue.  
- I am deeply curious about MACHINE LEARNING RESEARCH, the way we present and consume information, and natural language processing. 
- I enjoy walking, buskers, cold plunging, '67-'73 Chevy trucks, and Chagaccino! 

### Project Overview:
* App code is TBD 
* The app is containerized into a Docker image  
* The Dockerfile uses TBD to compile the app code and copies the binary into a minimal final image
* The app can be manually deployed using flyctl from the fly.toml config file
* GitHub Actions deploys main to dev automatically

```bash
src/
├── open/                # ELv2 Licensed Components
│   ├── interfaces/      # Public interfaces
│   ├── types/           # Common type definitions
│   ├── utils/           # General utilities
│   └── models/          # Base model definitions
│
├── proprietary/         # Proprietary Components
│   ├── core/            # Core business logic
│   ├── ml/              # Machine learning implementations
│   ├── agents/          # Agent systems
│   └── processes/       # Business process implementations
│
└── commercial/          # Commercial Integration Points
    ├── adapters/        # Integration adapters
    └── services/        # Service implementations
```

### Tech stack:
* <?>  - for routing
* Parcel - for preprocessing SCSS
* <?> - for the app code
* Docker - for unit of deployment
* flyctl - for manual deployment
* GitHub Actions - for CI/CD
* Fly.io - for the serverless hosting platform
* Replicate - <perhapsfor AI with an API


```flyctl``` is a CLI tool from [Fly.io](http://fly.io)
You can read about it [here](https://fly.io/docs/hands-on/).

### History:  

### Roadmap: Effortless login, and the developer experience
[Q4](not available) Candidates:  
* Dynamic - suite for log in, wallet creation, and user management    
* SpruceID - a future where users control their identity & data    
* fission - identity, data, and compute solutions for the future of the Internet  
* Backstage - open source framework for developer experience
   
### Release 0.0.0  
In progress

### Acknowledgements:

This project [depends](https://github.com/kjon-life/vertispira/network/dependencies) on the copious contributions of others including:

- [Claude](https://claude.ai/project/)
- [Cursor](https://www.cursor.com/) on Darwin

This project is possible because of these and other services:

- [Porkbun](https://porkbun.com/) - Domain registration and DNS management
- [Fly.io](https://fly.io/) - Application hosting platform

This project is possible because of these and other people:

- [ ](URL) - for code and ideas

## Development Process

### Releases
We follow a structured release process aligned with natural cycles. For details, see:
- [Release Process](docs/process/release-process.md)
- [Changelog](CHANGELOG.md)
- [Security Policy](SECURITY.md)
- [Migration Guides](docs/migrations/)

### Version Schedule
- Feature Releases: Quarterly (Equinoxes/Solstices)
- Bug Fix Releases: As needed
- [View Release Calendar](docs/process/release-calendar.md)

### For Contributors
- [Contribution Guidelines](CONTRIBUTING.md)
- [Development Setup](docs/development/setup.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

___ 
## Legal & Intellectual Property

Rua Vertex™ ℠ is a registered brand of Rua Vertex, LLC. We're innovators in management consulting and machine learning research. While we love sharing and collaborating, we need to protect our intellectual property:

- Our name and brand marks are protected
- Our methods and technologies are proprietary
- Patents pending on our processes and systems
- All rights reserved on our creative works

For detailed information, see:
- [LEGAL.md](./LEGAL.md) - Complete IP notice and usage rights
- [PATENTS.md](./PATENTS.md) - Patent and innovation protection
- [LICENSE](./LICENSE) - Terms of use

Questions? Reach out to legal@ruavertex.com

© 2024 Rua Vertex, LLC