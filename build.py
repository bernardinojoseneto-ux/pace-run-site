# Gera as páginas do site do Pace Run (cabeçalho e rodapé iguais em todas). Uso: python3 build.py
import pathlib

EMAIL = 'bernardino.joseneto@gmail.com'
OWNER = '<span class="todo">[NOME DO RESPONSÁVEL]</span>'
CITY = '<span class="todo">[CIDADE/UF]</span>'
UPDATED = '21 de outubro de 2026'
MARK = ('<svg viewBox="0 0 100 100" aria-hidden="true"><defs><mask id="h"><rect x="-50" y="-50" width="200" height="200" fill="#fff"/>'
        '<circle cx="30" cy="86" r="4" fill="#000"/></mask></defs><g mask="url(#h)" transform="translate(-4 -2)">'
        '<path d="M30 86 V14 H58 C74 14 82 24 82 36 C82 48 74 58 58 58 H46" fill="none" stroke="#F0782E" stroke-width="12" '
        'stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="86" r="10" fill="#F0782E"/></g></svg>')
PAGES = [('index.html', 'Início'), ('privacidade.html', 'Privacidade'), ('termos.html', 'Termos'), ('suporte.html', 'Suporte')]


def page(file, title, desc, body):
    nav = ''.join(f'<a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{n}</a>' for f, n in PAGES)
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0A">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<main>
<header class="top">
<a class="brand" href="index.html" aria-label="Pace Run, início">{MARK}<b>PACE</b><span>RUN</span></a>
<nav aria-label="Páginas">{nav}</nav>
</header>
{body}
<footer>Pace Run · contato: <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="privacidade.html">Privacidade</a> · <a href="termos.html">Termos</a></footer>
</main>
</body>
</html>
'''


INDEX = f'''
<section class="hero">
{MARK}
<h1>Corra com dados em que você confia.</h1>
<p class="lead">O Pace Run grava suas corridas por GPS ou na esteira, acompanha sua meta da semana e monta um plano que respeita seu corpo. Seu histórico é seu.</p>
<div class="grid">
<div class="card"><h3>Corrida ao vivo</h3><p>Distância, ritmo, velocidade e elevação, com aviso por voz a cada km.</p></div>
<div class="card"><h3>Plano adaptativo</h3><p>5, 10 ou 21 km, com pausa por dor, doença ou viagem e retomada gradual.</p></div>
<div class="card"><h3>Privacidade</h3><p>Rotas privadas por padrão e zonas ocultas de casa e trabalho.</p></div>
<div class="card"><h3>Seus dados</h3><p>Exporte tudo em GPX ou CSV quando quiser, de graça.</p></div>
</div>
</section>
<p>Em breve para iPhone e Android. Dúvidas: <a href="suporte.html">Suporte</a>.</p>
'''

PRIVACY = f'''
<p class="kicker">Atualizada em {UPDATED}</p>
<h1>Política de privacidade</h1>
<p>O Pace Run coleta só o necessário para gravar suas corridas e guardar seu histórico. Não vendemos seus dados, não mostramos anúncios e não usamos ferramentas de rastreamento de terceiros.</p>

<h2>Quem é o responsável</h2>
<p>O controlador dos dados, nos termos da Lei Geral de Proteção de Dados (Lei 13.709/2018), é {OWNER}, {CITY}. Contato do encarregado: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

<h2>Quais dados usamos e para quê</h2>
<table>
<thead><tr><th>Dado</th><th>Para quê</th><th>Onde fica</th></tr></thead>
<tbody>
<tr><td>E-mail</td><td>Entrar na conta com um código enviado por e-mail</td><td>Servidor (se você criar conta)</td></tr>
<tr><td>Localização (GPS)</td><td>Medir distância, ritmo e o trajeto das corridas, inclusive com a tela bloqueada <strong>durante a corrida</strong></td><td>No aparelho; o trajeto vai para o servidor com o backup</td></tr>
<tr><td>Corridas (data, duração, distância, elevação, velocidade, parciais, trajeto, altimetria)</td><td>Histórico, metas, recordes, previsões e Story</td><td>No aparelho; no servidor com o backup</td></tr>
<tr><td>Perfil (nível, metas, preferências de voz, calibração da esteira)</td><td>Personalizar metas, plano e avisos</td><td>No aparelho; no servidor com o backup</td></tr>
<tr><td>Peso e idade (opcionais)</td><td>Calcular calorias</td><td>No aparelho; no servidor com o backup</td></tr>
<tr><td>Plano de treino</td><td>Mostrar e ajustar seus treinos</td><td>No aparelho; no servidor com o backup</td></tr>
<tr><td>Sensores de movimento e barômetro</td><td>Contar passos na esteira e medir elevação</td><td>Só no aparelho</td></tr>
<tr><td>Zonas ocultas (casa e trabalho)</td><td>Esconder o trecho perto delas no Story</td><td>Só no aparelho, nunca no servidor</td></tr>
<tr><td>Fotos e câmera</td><td>Fundo do Story, só quando você escolhe</td><td>Só no aparelho</td></tr>
</tbody>
</table>
<p>Sem conta, tudo fica apenas no seu aparelho. Com conta, o app faz backup no servidor para você não perder nada ao trocar de celular. A base legal é a execução do serviço que você pediu e, para localização, fotos e sensores, o seu consentimento, dado nas permissões do sistema e revogável a qualquer momento nos Ajustes do celular.</p>
<p><strong>Dados de saúde:</strong> peso, idade e o desempenho nas corridas podem ser considerados dados sensíveis. Usamos esses dados só para as funções descritas acima, com o seu consentimento, e você pode apagá-los quando quiser.</p>

<h2>Com quem compartilhamos</h2>
<p>Usamos serviços que processam dados em nosso nome, só para o app funcionar:</p>
<ul>
<li><strong>Supabase</strong>: banco de dados e login. Servidor em São Paulo, Brasil.</li>
<li><strong>Resend</strong>: envio do e-mail com o código de acesso (recebe só o seu e-mail).</li>
<li><strong>Apple Maps (iPhone) e Google Maps (Android)</strong>: desenham o mapa com ruas. Recebem a região do mapa exibida, não o seu histórico.</li>
</ul>
<p>O Story é gerado no seu aparelho e só sai dele quando você escolhe compartilhar. Nele, o início e o fim do trajeto e as zonas ocultas não aparecem.</p>

<h2>Por quanto tempo guardamos</h2>
<p>Enquanto sua conta existir. Ao excluir a conta, seus dados são apagados do servidor na hora. Dados que ficam só no aparelho saem quando você apaga o app ou usa "Apagar dados deste aparelho".</p>

<h2>Seus direitos</h2>
<p>Você pode, a qualquer momento:</p>
<ul>
<li><strong>Acessar e levar seus dados:</strong> em Você › Exportar dados (GPX e CSV).</li>
<li><strong>Corrigir:</strong> metas, peso e idade em Você.</li>
<li><strong>Excluir:</strong> uma corrida no histórico, ou a conta inteira em Você › Conta e backup › Excluir minha conta.</li>
<li><strong>Revogar permissões:</strong> nos Ajustes do celular.</li>
<li><strong>Pedir informações ou fazer outra solicitação:</strong> pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. Respondemos em até 15 dias.</li>
</ul>
<p>Se achar que seus direitos não foram atendidos, você pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>Crianças e adolescentes</h2>
<p>O app é para maiores de 12 anos. Menores de 18 devem usá-lo com autorização dos pais ou responsáveis.</p>

<h2>Segurança</h2>
<p>A conexão com o servidor é criptografada e cada pessoa só tem acesso aos próprios dados. Nenhum sistema é 100% seguro: se houver um incidente que afete você, avisaremos.</p>

<h2>Mudanças nesta política</h2>
<p>Se mudarmos algo importante, avisaremos no app antes de valer. A data no topo indica a última atualização.</p>
'''

TERMS = f'''
<p class="kicker">Atualizados em {UPDATED}</p>
<h1>Termos de uso</h1>
<p>Ao usar o Pace Run, você concorda com estes termos. Leia também a <a href="privacidade.html">política de privacidade</a>.</p>

<h2>O que é o Pace Run</h2>
<p>Um app para gravar corridas, acompanhar metas e seguir planos de treino. O app é oferecido por {OWNER}, {CITY}.</p>

<h2>Saúde e segurança</h2>
<ul>
<li>O Pace Run <strong>não é um dispositivo médico</strong> e não substitui orientação de médico, fisioterapeuta ou educador físico.</li>
<li>Os planos e as orientações são <strong>educativos</strong>. Antes de começar a treinar, principalmente se você tem alguma condição de saúde, consulte um médico.</li>
<li>Pare a atividade se sentir dor, falta de ar, tontura ou mal-estar. Dor que dura mais de uma semana ou piora: procure um profissional.</li>
<li>Corra com atenção ao trânsito e ao ambiente. Não mexa no celular enquanto corre em locais perigosos.</li>
</ul>

<h2>Precisão dos dados</h2>
<p>Distância, ritmo, elevação, calorias e previsões são estimativas. O GPS pode errar em prédios altos, túneis e com sinal fraco, e a esteira depende da calibração.</p>

<h2>Sua conta</h2>
<p>Você é responsável pelo acesso ao seu e-mail, usado para entrar no app. Pode excluir a conta quando quiser, em Você › Conta e backup.</p>

<h2>Uso correto</h2>
<p>Não use o app para fins ilegais, para tentar acessar dados de outras pessoas ou para atrapalhar o funcionamento do serviço.</p>

<h2>Preço</h2>
<p>O app é gratuito hoje. Se surgirem recursos pagos, eles serão opcionais e avisados com antecedência. Exportar seus dados continuará gratuito.</p>

<h2>Disponibilidade e mudanças</h2>
<p>Trabalhamos para o app funcionar sempre, mas pode haver falhas ou interrupções. Podemos mudar recursos e estes termos; mudanças importantes serão avisadas no app.</p>

<h2>Lei e foro</h2>
<p>Estes termos seguem as leis do Brasil, incluindo o Código de Defesa do Consumidor. Fica eleito o foro do seu domicílio.</p>
'''

SUPPORT = f'''
<h1>Suporte</h1>
<p>Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>. Respondemos em até 3 dias úteis.</p>

<h2>Perguntas frequentes</h2>
<h3>O código de acesso não chegou</h3>
<p>Ele pode levar até 1 minuto. Veja também a caixa de spam e promoções. Se não chegar, toque em "Trocar e-mail", confira o endereço e peça de novo.</p>
<h3>Preciso de senha?</h3>
<p>Não. Você entra com um código de 6 dígitos enviado por e-mail e continua conectado até sair da conta.</p>
<h3>Troquei de celular. Como recupero minhas corridas?</h3>
<p>Instale o app, toque em "Já tenho conta" e entre com o mesmo e-mail. Suas corridas, metas e plano voltam sozinhos.</p>
<h3>A corrida parou de gravar com a tela bloqueada</h3>
<p>Permita a localização "Ao usar o app" e confira se a economia de bateria não está fechando o app. No Android, desative a otimização de bateria para o Pace Run.</p>
<h3>A distância na esteira está diferente do painel</h3>
<p>Ao terminar, informe a distância do painel. O app aprende e corrige as próximas corridas.</p>
<h3>Como exporto meus dados?</h3>
<p>Em Você › Exportar dados, em GPX (para outros apps) ou CSV (planilha).</p>
<h3>Como excluo minha conta?</h3>
<p>Em Você › Conta e backup › Excluir minha conta. Isso apaga a conta, as corridas e o plano do servidor e do celular, e não pode ser desfeito. Se não conseguir pelo app, escreva para <a href="mailto:{EMAIL}">{EMAIL}</a> com o assunto "Excluir conta", do e-mail da conta.</p>
'''

out = pathlib.Path(__file__).parent
for file, title, desc, body in [
    ('index.html', 'Pace Run · app de corrida', 'App de corrida com GPS, metas semanais e plano adaptativo.', INDEX),
    ('privacidade.html', 'Política de privacidade · Pace Run', 'Como o Pace Run trata seus dados (LGPD).', PRIVACY),
    ('termos.html', 'Termos de uso · Pace Run', 'Termos de uso do Pace Run.', TERMS),
    ('suporte.html', 'Suporte · Pace Run', 'Ajuda e contato do Pace Run.', SUPPORT),
]:
    (out / file).write_text(page(file, title, desc, body), encoding='utf-8')
(out / 'favicon.svg').write_text(MARK.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'), encoding='utf-8')
print('ok')
