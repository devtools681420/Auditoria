# PMJA - Gestão de Instrumentos e Certificados de Calibração

Este é um aplicativo web desenvolvido com Streamlit para gerenciar e visualizar certificados de calibração de instrumentos.

## Descrição

O sistema permite a busca e visualização de certificados de calibração de instrumentos a partir de uma planilha Excel. Os dados são apresentados em um formato de cards com informações detalhadas sobre cada instrumento e seu respectivo certificado.

## Funcionalidades

- Interface web intuitiva para busca de certificados de calibração
- Visualização em formato de cards com imagem e detalhes do instrumento
- Sistema de busca que permite filtrar por qualquer campo dos dados
- Links interativos para acesso direto aos certificados
- Layout responsivo que se adapta a diferentes tamanhos de tela
- Normalização de texto para buscas mais eficientes (remoção de acentos e caracteres especiais)

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Excel](https://products.office.com/excel) (para armazenamento de dados)

## Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/Auditoria.git
   cd Auditoria
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   streamlit run app.py
   ```

## Estrutura do Projeto

- `app.py` - Código principal do aplicativo Streamlit
- `PMJA_Controle Certificados de calibração_V_2.xlsm` - Arquivo de dados Excel
- `requirements.txt` - Lista de dependências do Python
- `.gitignore` - Arquivos e diretórios ignorados pelo Git
- `README.md` - Este arquivo
- `LICENSE` - Arquivo de licença do projeto

## Configuração do Arquivo de Dados

O aplicativo espera encontrar um arquivo Excel chamado `PMJA_Controle Certificados de calibração_V_2.xlsm` na raiz do projeto com as seguintes colunas:

- Informações gerais sobre os instrumentos
- Coluna opcional "Link" para acesso direto aos certificados
- Coluna opcional "ImagemLink" para exibição de imagens dos instrumentos

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autor

Daniel Albuquerque