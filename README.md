# scrap-dados-imovelweb
<p>Scrap de dados de anúncio no Imovelweb</p>
</br>
 Scrap de dados desenvolvido em Python utilizando Selenium com o seguinte fluxo:
 <ul>
  <li>Carrega arquivo .txt com os links que deseja pegar os dados</li>
  <li>Carrega planilha do Excel e verifica se a mesma já possui dados na tabela, caso positivo, o código vai incluir os dados abaixo dos atuais</li>
  <li>Inicia Selenium entrando em cada link incluído no arquivo .txt</li>
  <li>Dentro do selenium, verifica se as variáveis endereço, nome do corretor, valor de venda, área construída, quantidade de dormitórios, banheiros e vagas</li>
  <li>Ainda dentro do selenium, executa script para habilitar telefone do corretor</li>
  <li>Inclui as variáveis obtidas na planilha Excel e finaliza Selenium</li>
 </ul>
