<p align="center">
  <img src="https://github.com/citi-onboarding/Engaj/blob/develop/static/img/logos/engaj-verde-alt.svg" width="350" title="Engaj">
</p>
<p align=center>
  <img src=https://img.shields.io/badge/Status-WIP-green.svg?style=for-the-badge&colorB=8cbc4e>
  <img src=https://img.shields.io/badge/PSC-2018.2-green.svg?style=for-the-badge&colorB=8cbc4e>
</p>

A ENGAJ é a empresa Júnior do curso de Engenharia Ambiental da USP São Carlos. Essa one-page foi construída durante o PSC 2018.2. Preview: http://engaj-staging.herokuapp.com/

## Primeiros passos
Siga estes passos, caso queira ter uma cópia do projeto configurada e executando no seu host local, para propósitos de desenvolvimento e testes. Veja a seção [`Realizando Deploy`](#realizando-deploy) para entender como fazer a instalação em um ambiente de produção.

### Requisitos
É necessário possuir `python3` e `virtualenv` instalandos. Caso não os possua, é possível obtê-los (no Ubuntu) pelo comando:

```
sudo apt install python3 virtualenv -y
```

### Ambiente para desenvolvimento
#### Ubuntu e Derivados
Inicialmente, obtenha o código da aplicação. Utilizando o git, você teria algo assim:

```
git clone https://github.com/citi-onboarding/Engaj.git
```

entre no diretório `Engaj/`:

```
cd Engaj/
```

Crie uma pasta para o ambiente virtual:

```
mkdir env/
```

Crie o ambiente virtual. Nesse caso, usando o `virtualenv` no Linux, basta executar:

```
virtualenv env/ -p python3
```
Ative-o:

```
source env/bin/activate
```

Instale todas as dependências contidas no `requirements.txt`

```
pip install -r requirements.txt
```
Uma configuração adicional que precisa ser realizada inclui definir uma variável de ambiente `DROPBOX_ACCESS_TOKEN` com o token de acesso para algum app registrado no dropbox. Para criar um app e obter um token, acesse https://www.dropbox.com/developers/apps.

Após isso, você pode proceder de duas maneiras. Uma delas é registrar a variável de ambiente de modo a ser válida apenas na seção atual (será apagada ao reiniciar o sistema). Se optar por isso, basta fazer:

```
export DROPBOX_ACCESS_TOKEN=tokenDeAcesso
```
A outra opção é adicionar ao arquivo `.bashrc`, caso use Bash, esse mesmo comando. Para mais informações, veja [esse](https://www.vivaolinux.com.br/artigo/Trabalhando-com-shell-e-variaveis-de-ambiente?pagina=2) artigo.

Ao fim do processo, você pode testar se tudo foi corretamente instalado executando:
```
python manage.py migrate && python manage.py runserver
```
Após isso, basta acessar o endereço https://locahost:8000 em um navegador como Chrome, Firefox ou Safari. 

PS.: Caso queria a experiência completa, crie um usuário administrador por meio do comando
```
python manage.py createsuperuser
```
E adicione conteúdo ao site no painel de administração em https://localhost:8000/admin.

## Realizando Deploy
Veja [Deploy com Heroku](https://devcenter.heroku.com/articles/github-integration#enabling-github-integration) para mais informações

## Ferramentas

* [Django](https://www.djangoproject.com/) - The Web framework for perfectionists with deadlines
* [Virtualenv](https://virtualenv.pypa.io/en/latest/) - Ferramenta de criação dos ambientes virtuais em python
* [Slick](http://kenwheeler.github.io/slick/) - Framework para criação dos carrosseis
* [Parallax.js](http://pixelcog.github.io/parallax.js/) - Script para fazer o efeito de parallax
* [Django Storage](https://django-storages.readthedocs.io/en/latest/) - Biblioteca para mudar onde os arquivos de mídia são armazenados
* [Heroku](https://dashboard.heroku.com/) - Plataforma usada para deploy

## Desenvolvedores

* **Júnior Mendes** - [jrmmendes](https://github.com/jrmmendes)
* **Ana Beatriz** - [abcr98](https://github.com/abcr98)
* **Lucas Zacarias** - [lucaszsd](https://github.com/lucaszsd)

## Gerente
* **João Felix** - [jvbfelix](https://github.com/jvbfelix)
