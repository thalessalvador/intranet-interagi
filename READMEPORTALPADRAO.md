<div align="center"><img alt="logo" src="https://raw.githubusercontent.com/plonegovbr/plonegovbr.portal/main/docs/logo.png" width="100" /></div>

<h1 align="center">Portal Brasil</h1>

<div align="center">

[![GitHub contributors](https://img.shields.io/github/contributors/plonegovbr/plonegovbr.portal)](https://github.com/plonegovbr/plonegovbr.portal)
[![GitHub Repo stars](https://img.shields.io/github/stars/plonegovbr/plonegovbr.portal?style=social)](https://github.com/plonegovbr/plonegovbr.portal)

</div>
<a name="ancora"></a>
# Conteúdo

- [Introdução](#introdução)
- [Funcionalidades Especializadas](#funcionalidades-especializadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Inicialização](#inicialização)
- [Estrutura](#estrutura)
- [Licença](#licença)

## Introdução

O [Portal Brasil](https://plone.org.br/projetos/portal-brasil) é a distribuição Plone que contempla casos de uso do sistema de gestão de conteúdo [Plone](https://plone.org) para organizações brasileiras.

Sucessor tecnológico do [Portal Modelo](https://plone.org.br/projetos/portal-modelo) e do [Portal Padrão](https://plone.org.br/projetos/portal-padrao), a distribuição oferece aos seus usuários:

* Tipos de conteúdo especializados
* Conteúdos de Exemplo
* Design padronizado, mas com possibilidade de pequenos ajustes

## Funcionalidades Especializadas
* Serviços
* Pessoas
* Agenda
* Notícias


## Pré-Requisitos

- Python 3.9, 3.10, 3.11
- Node 16
- yarn
- Docker
- Veja mais detalhes em [Install Plone from its packages](https://6.docs.plone.org/install/install-from-packages.html)

## Instalação

```shell
git clone git@github.com:plonegovbr/plonegovbr.portal.git
cd portal-brasil
make install
```

## Inicialização

Inicialização do Backend (http://localhost:8080/)

```shell
make start-backend
```

Inicialização do Frontend (http://localhost:3000/)

```shell
make start-frontend
```

## Estrutura

Há duas bases de código no diretório: backend(API) e frontend.

- **backend**: API (Backend) Instalação do Plone usando pip.
- **frontend**: React (Volto) 

## Considerações

- O repositório contém todo o código necessário para rodar o site.


## Licença

Esse projeto é licenciado sob a licença GPLv2.
