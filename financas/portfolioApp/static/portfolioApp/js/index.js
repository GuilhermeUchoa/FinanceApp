const valorTotal = parseFloat(document.querySelector("#valorTotal").innerHTML)

//Calculo da porcentagem de cada ativo
function porcentagemCalc(){
    document.querySelectorAll("tbody tr").forEach((item)=>{
        let valor = item.querySelector("#valor")
        let porcentagem = item.querySelector("#porcentagem")
        let valorTotalToPercent = parseFloat(document.querySelector("#valorTotal").innerHTML)
        porcentagem.innerHTML = (parseFloat(valor.innerHTML)/valorTotalToPercent*100).toFixed(2)
        
    })
}

//cota aporte valor valortotal porcentagem
function cotaAporteValorTotalPorcentagem(){
    let tr = event.currentTarget.parentNode.parentNode
    let cota = parseFloat(tr.querySelector("td input#cota").value)
    let cotacao = parseFloat(tr.querySelector("#cotacao").innerHTML)
    let quantidade = parseFloat(tr.querySelector("#quantidade").innerHTML)

    //aporte
    tr.querySelector("#aporte").innerHTML = (cota * cotacao).toFixed(2)
    
    //valor
    tr.querySelector("#valor").innerHTML = ((cota+quantidade) * cotacao).toFixed(2)


    //valorTotal
    const cells_valor = document.querySelectorAll("tbody tr td#valor")
    const valores = Array.from(cells_valor).map(cell => parseFloat(cell.textContent));
    const valorT = valores.reduce((total, valor) => total += valor, 0);
    document.querySelector("#valorTotal").innerHTML = parseFloat(valorT).toFixed(2)



    //aporte
    document.querySelector("#aporteTotal").innerHTML = (valorT - valorTotal).toFixed(2)

    //porcentagem
    porcentagemCalc()

}

//metaTotal
function metaTotalCalc(){
    const cells_metas = document.querySelectorAll("tbody tr td input#meta")
    const metas = Array.from(cells_metas).map( cell=>parseFloat(cell.value))
    const metaTotal = metas.reduce((total,valor)=> total + valor ,0)
    document.querySelector("#metaTotal").innerHTML = parseFloat(metaTotal).toFixed(2)
}



function porcentagemQuadroGeral(){
  
  console.log(document.querySelector("#acaoPorcentagem").innerHTML)

  acaoValor = parseFloat(document.querySelector("#acaoValor").innerHTML.replace("R$","").replace(",",""))
  document.querySelector("#acaoPorcentagem").innerHTML = (parseFloat(acaoValor/valorTotal)*100).toFixed(2)

  bdrValor = parseFloat(document.querySelector("#bdrValor").innerHTML.replace("R$","").replace(",",""))
  document.querySelector("#bdrPorcentagem").innerHTML = (parseFloat(bdrValor/valorTotal)*100).toFixed(2)

  fiiValor = parseFloat(document.querySelector("#fiiValor").innerHTML.replace("R$","").replace(",",""))
  document.querySelector("#fiiPorcentagem").innerHTML = (parseFloat(fiiValor/valorTotal)*100).toFixed(2)

}

function onInit(){

  porcentagemCalc()
  metaTotalCalc()
  porcentagemQuadroGeral()
}

window.onload = onInit()



// Filtro
const myFunction = () => {
    const trs = document.querySelectorAll('#myTable tr:not(.header)')
    const filter = document.querySelector('#myInput').value
    const regex = new RegExp(filter, 'i')
    const isFoundInTds = td => regex.test(td.innerHTML)
    const isFound = childrenArr => childrenArr.some(isFoundInTds)
    const setTrStyleDisplay = ({ style, children }) => {
      style.display = isFound([
        ...children // <-- All columns
      ]) ? '' : 'none' 
    }
    
    trs.forEach(setTrStyleDisplay)
  }

// Para fazer o fetch que substitui o ajax é necessario
// 1 mapear os elementos da pagina
// 2 atribuir eventlistener
// criar o fetch e modificar o elemento que vc tenha interesse