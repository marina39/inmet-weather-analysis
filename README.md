# Análise de Dados Meteorológicos históricos INMET

## Selenium

```
  from selenium.webdriver.chrome.service import Service
  from selenium.webdriver.chrome.options import Options
  from webdriver_manager.chrome import ChromeDriverManager 
```

**Service**: gerencia o ciclo de vida do executável do Driver, controlando a abertura e o fechamento do processo .exe

**Options**: configura o comportamento do navegador (ex: tela cheia, modo anônimo).

**ChromeDriverManager**: identifica e baixa automaticamente o driver compatível com a versão do navegador do computador.

<br>

```
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=options)
```

O gerenciador localiza o caminho exato (**path**) do driver está no computador;

O **path** é entregue ao **Service**;

O **webdriver.Chrome** recebe o path pronto, garantindo a inicialização estável.

<br>

> **Por que usar a modulação mais robusta?**
> 
> Com o uso do ambiente virtual (empacotamento) o Python pode acabar se 'perdendo' e não encontrar o driver.
