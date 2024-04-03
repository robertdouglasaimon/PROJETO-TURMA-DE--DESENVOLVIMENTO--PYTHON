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

