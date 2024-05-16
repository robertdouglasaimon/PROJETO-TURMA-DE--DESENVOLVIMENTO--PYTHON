// MENU DE CRONOGRAMA / EXERCICIOS
function openMenu(evt, menuName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("menu");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" w3-dark-grey", "");
    }
    document.getElementById(menuName).style.display = "block";
    evt.currentTarget.firstElementChild.className += " w3-dark-grey";
  }
  document.getElementById("myLink").click();


  // ANIMAÇÃO DE ESCREVER DO TEXTO DO TOPO
  var typingElement = document.getElementById('typing');
  var text = '"Em apenas 10 dias, mergulhamos na lógica de programação e desenvolvimento de aplicativos usando uma das linguagens mais versáteis e poderosas do mundo da programação."';
  var index = 0;

  // Define a função para simular a digitação do texto
  function typeWriter() {
      if (index < text.length) {
          typingElement.innerHTML += text.charAt(index);
          index++;
          typingElement.scrollTop = typingElement.scrollHeight; // Role automaticamente para a parte inferior
          setTimeout(typeWriter, Math.floor(Math.random() * 150) + 50); // Ajuste o intervalo conforme desejado
      } else {
        // Reinicia o índice para recomeçar o texto
        index = 0;
        // Limpa o conteúdo da div para recomeçar a digitação
        typingElement.innerHTML = "";
        // Chama novamente a função para iniciar a digitação
        setTimeout(typeWriter, 3000); // Aguarde 3 segundo antes de recomeçar
    }
}


  // Chama a função para iniciar a digitação
  typeWriter();

  // Define as keyframes para a animação de piscar
  var blinkKeyframes = "@keyframes blink { 50% { border-color: transparent; } }";

  // Cria um estilo no cabeçalho da página para incluir os keyframes
  var styleElement = document.createElement("style");
  styleElement.innerHTML = blinkKeyframes;
  document.head.appendChild(styleElement);






  
  document.addEventListener('DOMContentLoaded', (event) => {
    openMenu(event, 'Conteudo');
});


//-----------------------------------------------------------------------------//


// Seletor de mídia
const mediaQuery = window.matchMedia("(max-width: 653px) and (max-height: 615px)");

// Função para manipular a mudança de mídia
const handleMediaChange = (mediaQuery) => {
  if (mediaQuery.matches) {
    // Se a condição de mídia for atendida, oculte a imagem bgimg e mostre a imagem pqimg
    document.getElementById('bgimg').style.display = 'none';
    document.getElementById('pqimg').style.display = 'block';
  } else {
    // Se a condição de mídia não for atendida, reverta as alterações
    document.getElementById('bgimg').style.display = 'block';
    document.getElementById('pqimg').style.display = 'none';
  }
};

// Adicionar ouvinte de evento para a mudança de mídia
mediaQuery.addListener(handleMediaChange);

// Chamar a função uma vez para garantir que os estilos sejam aplicados corretamente inicialmente
handleMediaChange(mediaQuery);



//----------------------------------------------------------------------------//