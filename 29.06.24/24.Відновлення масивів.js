process.stdin.on('data', function (data) {
  let n = data.toString();
  let x = n.replace(/(\r\n|\n|\r)/gm, " ").trim().split(' ')
  const N = Number(x.shift());
  const M = Number(x.shift());
  x = x.map(el=>Number(el))

  const list = []
  for(let i = 0; i<x.length/3; i++){
    list[i] = x.slice(i*3, i*3+3)
  }

  let resultArr = new Array(N);
  let check = false;

  while(!check){
    check = true;

    for(let i = 0; i<M; i++){

      //якщо обидва не заповнені
      if(!resultArr[list[i][0]-1] && !resultArr[list[i][1]-1]){
        resultArr[list[i][0]-1] = list[i][2];
        resultArr[list[i][1]-1] = list[i][2]+1;
      }

      //якщо перший
      if(resultArr[list[i][0]-1] && !resultArr[list[i][1]-1]){
        if(resultArr[list[i][0]-1]>=list[i][2]){
          resultArr[list[i][1]-1] = list[i][2]
          check = false
        }else{
          resultArr[list[i][0]-1]= list[i][2]
        }
      } 

      //якщо другий
      if(!resultArr[list[i][0]-1] && resultArr[list[i][1]-1]){
        if(resultArr[list[i][1]-1]>=list[i][2]){
          resultArr[list[i][0]-1] = list[i][2]
          check = false
        }else{
          resultArr[list[i][1]-1]= list[i][2]
        }
      }

      //якщо обидва заповнені
      if(resultArr[list[i][0]-1] && resultArr[list[i][1]-1]){
        if(resultArr[list[i][0]-1] != list[i][2] && resultArr[list[i][1]-1] != list[i][2] ){
          check = false;
          if(resultArr[list[i][0]-1]>list[i][2] && resultArr[list[i][0]-1]>resultArr[list[i][1]-1] ){
            resultArr[list[i][1]-1] = list[i][2]
          }
          if(resultArr[list[i][1]-1]>list[i][2] && resultArr[list[i][1]-1]>resultArr[list[i][0]-1] ){
            resultArr[list[i][0]-1] = list[i][2]
          }
        }
        if(resultArr[list[i][0]-1] == list[i][2] && resultArr[list[i][1]-1] < list[i][2] || 
          resultArr[list[i][1]-1] == list[i][2] && resultArr[list[i][0]-1] < list[i][2]){
          check = false;
        }
      }   
     
    }

  }
  const result = resultArr.join(" ")

  process.stdout.write(result); 
});
