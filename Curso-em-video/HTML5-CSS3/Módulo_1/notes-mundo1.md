# Curso HTMl-CSS | anotações

### Parágrafos e quebras de linha

Você pode escrever um paragrafo colocando tudo no meio de tags p e /p

Se precisar quebrar o texto em algum lugar especifico, você coloca a tag &lt;br&gt;

adicionar alguns símbolos especiais:
&reg;
&copy;
&trade;
&euro;

adicionar alguns emojis:
&#x1F596;
&#x1F913;


### Testando cargas de imagens

imagens que está na mesma pasta --> link da imagem

carregar imagens que estão em sub-pastas --> ../img

Também podemos carregar imagens externas --> copia o link da imagem 

### Favicon

coloca o link da imagem no head, com a tag link:

link rel="shortcut icon" href="Link do favicon" type="image/x-icon"

### Hierarquia de títulos

- h1 --> título de nível 1 
- h2 --> título de nível 2
- h3 --> título de nível 3
- h4 --> título de nível 4

### Principais formatações

**Negrito / destaque:** 

negrito usando a tag b (Não semântica)
termo em destaque usando a tag strong (semântica)

**Itálico / enfâse:**

termo em itálico usando a tag i (Não semântica)
termo em enfâse usando a tag em (semântica) 

**Texto marcado:**

um texto marcado usando a tag mark

**Texto grande e pequeno:** 

texto pequeno usando a tag small

Texto deletado: usando a tag del

**Texto inserido:** 

usando a tag ins, para da uma enfâse e indicar que ele foi adicionado depois. existe também o sulinhado com a tag u

**Texto sobrescrito:**

para inserir coisas do tipo x²+3 usamos a tag sup
para inserir coisas do tipo H2O usamos a tag sub

### cóigo-fonte / pré-formatação

usamos a tag code

```
    <pre>
        <code>
            num = int(input('digite um numero'))
            if num % 2 == 0:
                print(f'o numero {num} é par')
            else:
                print(f'o numero {num} é impar')
            print('fim do programa')
        </code>
    </pre>
```

**Citações:**
usamos a tag q

**Citações completas:**
usamos a  tag blockquote 


**Abreviações:**
usamos a tag abbr 

**Texto invertido:**
usamos a tag bdo 


### Trabalhando com listas

**listas ordenadas:**

```
<ol type=1, A,, a, I, i
    <li>acordar</li>
    <li>tomar café</li>
    <li>escovar os dentes</li>
    <li>Estudar programação</li>
</ol>
```

**listas não ordenadas:**

```
    <ul type="circle, disc, square">
        <li>pão</li>
        <li>arroz</li>
        <li>feijão</li>
    </ul>
```

**lista de definições:**

```
    <dl>
        <dt>html</dt>
        <dd>linguagem de marcação</dd>
        <dt>css</dt>
        <dd>linguagem de marcação de designe</dd>
        <dt>javascript</dt>
        <dd>linguagem de programação</dd>
    </dl>
```

### Trabalhando com links

```
                                                            <!--target e rel para abrir uma nova guia-->
<a href="https://github.com/maycondouglasbm?tab=repositories" target="_blank" rel="external'"></a>

<a href="https://instagram.com/maycondouglasbm10/">instagram</a></p> <!-- não abre uma nova guia-->
```

**usando links internos:**

```
<a href="pag02.html" target="_self" rel="next"></a>
<a href="noticiais/pag" rel="next"></a>
```

**links para dowloads:**

```
<ul>
    <li><a href="link do pdf" download="meulivro.pdf" type="application/pdf">baixar</a> links para pdf</li>
    <li><a href="link do compactado em zip">livro</a> compactado em zip</li>
</ul>
```

**Imagens dinamicas:**

```
    <picture>                     <!--não esquecer de colocar o max-width-->
        <source media="(max-width: 300)" srcset="imagens/foto-p.png" typw="image/png" >
        <source media="(max-width: 750)" srcset="imagens/foto-g.png" type="image/png">
        <source media="(max-width:1050)" srcset="imagens/foto-m.png" type="image/png">
        <img src="imagens/foto-g.png" alt="imagem flexivel">
    </picture>
```
**Audio:**

```
    <audio src="" controls autoplay></audio>
    <audio preload="none" controls autoplay loop>
        <source src="midia/guanacast-33.mp3" type="audio/mpeg"> <!--wav é pesado-->
        <p>Seu navegador não suporta áudio <a href="midia/guanacast-33.mp3" download="guanacast-33.mp3" type="audio/mpeg"></a></p>
    </audio>
```

### Inserindo vídeos hospedados localmente

**hospedado no meu próprio servidor**

 ```
    <video width="600" poster="imagens/limoes-capa.png" controls autoplay loop>
        <source src="midia/meu-video.webm" type="video/webm">
        <source src="midia/meu-video.mp4" type="video/mp4">
        <source src="midia/meu-video.ogv" type="video/ogg">
        <p>Infelizmente seu navegador nao conseguiu carregar o vídeo.</p>
    </video>
```

**Inserindo vídeos do Youtube:**

```
    <iframe width="600" height="315" src="https://www.youtube.com/embed/kQ-4bgu2htk" 
    title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write;
    encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```