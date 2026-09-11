document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("pre.mermaid").forEach(function (pre) {
    var code = pre.querySelector("code");
    var text = code ? code.textContent : pre.textContent;
    var div = document.createElement("div");
    div.className = "mermaid";
    div.textContent = text;
    pre.replaceWith(div);
  });

  mermaid.initialize({ startOnLoad: false });
  mermaid.run();
});