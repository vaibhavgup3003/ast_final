const menu = document.querySelector("select");

const divs = document.querySelectorAll("div");

menu.addEventListener("change", (e) => {
  const val = menu.value;
  console.log(val)
  for (let div of divs) {
    console.log(div.id)
    if (div.id === val) {
      div.classList.remove("hide");
    } else {
      div.classList.add("hide");
    }
  }
});

document.querySelector('#create button').addEventListener('click', e=>{
    const input=document.querySelectorAll("#create input");
    const rule_name=input[0].value
    const rule_def=input[1].value
    input.value=''

    fetch(`http://127.0.0.1:8000/process?rule_name=${rule_name}&input_string=${rule_def}`)
    .then(resp=>{
        alert(`Rule created with name ${rule_name}`)
    })
});

document.querySelector('#evaluate button').addEventListener('click', e=>{
    const input=document.querySelector('#evaluate input')
    const rule_name=input.value
    input.value=''

    const text=document.querySelector('#evaluate textarea')
    const json=JSON.parse(text.value)

    text.value=''

    fetch(
      `http://127.0.0.1:8000/evaluate/${rule_name}`,
      {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
      }
    ).then(resp=>{
        return resp.json()
    }).then(data=>{
        console.log(data)
        alert(`Evaluation result: ${data.result}`)
    })
});