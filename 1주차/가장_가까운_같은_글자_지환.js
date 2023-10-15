function solution(s) {
  var answer = [];
  let testObj = {};
  
  for (let i=0;i<s.length;i++) {
      if (s[i] in testObj) {
          answer.push(i - testObj[s[i]]);
          testObj[s[i]] = i;
      } else {
          testObj[s[i]] = i;
          answer.push(-1)
      }
  }
  return answer;
}