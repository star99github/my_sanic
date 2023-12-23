
var write_log_res = {"init": "default value"};


var header_obj = Vue.createApp({
    data() {
        return {
            msg:'欢迎来到应用管理平台'
        }
    }
}).mount('#header')
console.log("头部区块vue对象：", header_obj);


var content_obj = Vue.createApp({
    data() {
        return {
            msg:'当前管理的站点有: django, flask, fastapi, asnic, tronade',
            data: write_log_res
        }
    }
}).mount('#content')
console.log("内容区块vue对象：", content_obj);


const footer_obj = Vue.createApp({
  data() {
    return {
      showMessage: 4,
        detail: "关于站点管理平台 :",
    }
  }
}).mount('#footer')
console.log("底部区块vue对象：", footer_obj);


const u_content = document.getElementById("file_content");
u_content.addEventListener("submit", async(event) => {
    event.preventDefault()
    const u_input = u_content["file_content"].value
    // const response =
    await fetch("http://localhost:8005/record_log",{
        method: "POST",
        mode: "no-cors",  // 解决跨域
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ file_content: u_input }),
    })
    .then(response => {
        console.log("开始处理响应：")
        response.json()
        // 处理响应
        // if (response.status == "success"){
        //     alert("成功");
        // }
        // throw new Error(response.detail)
    })
    .then(data => {
        // 处理获取到的数据
        console.log("数据处理：" + data);
        write_log_res = data;
        // u_content["file_content"].value = "结果：" + data
        console.log("响应结果：" + write_log_res);
    })
    .catch(error => {
        // 处理错误
        console.log("异常：" + error);
    })
    .finally(() => {
        console.log("当前请求完成: ");
    });
    // alert(response.json());

});
