function solution(t, p) {
  var answer = 0;
  let len = p.length;
  
  for (let i=0;i<t.length-len+1;i++) {
      let newNum = t.slice(i,i+len);
      if (parseInt(newNum) <= parseInt(p)) {
          answer++;
      }
  }
  return answer;
}