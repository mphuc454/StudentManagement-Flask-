// $(document).ready(() => {
//   $("button").click(() => {
//     $("#div1").fadeToggle();
//     $("#div2").fadeToggle("slow");
//     $("#div3").fadeToggle(5000);
//   });
//   $("#flip").click(() => {
//     $("#pane").slideUp(2000).slideDown(2000);
//   });
//   $("#start_btn").click(() => {
//     $("div").animate({
//       left: "250px",
//     });
//   });
// });
fetch("https://jsonplaceholder.typicode.com/todos", {
  method: 'POST',
  headers:{
    'Content-Type':'application/json'
  },
  body: JSON.stringify({
      userId: 'Thăng trầm'
  })
})
  .then(res => {
    if(res.ok){
      return res.json();
    }else{
      console.log("Failed to fetch data");
    }
  })
  .then((data) => console.log(data));
