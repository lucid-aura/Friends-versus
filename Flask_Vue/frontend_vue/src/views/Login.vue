<template>
  <div class="custom-home">
    <form @submit="onSubmit" @reset="onReset" v-if="show">
        <input class="custom-login-input" id="id" name="id" v-model="form.id" placeholder="id"/>
        <input class="custom-login-input" type='password' id="pw" name="pw" v-model="form.pw" placeholder="pw"/>
        <input class="custom-login-btn" type='submit' value='login' />
        <button class="custom-login-btn" type='button' @click="signUp">SignUp</button>
    </form>
  </div>
</template>

<script>
//import PlayerInfo from "./PlayerInfo";
import axios from 'axios';
axios.defaults.withCredentials = true;
  export default {
    data() {
      return {
        form: {
          id: '',
          pw: '',
        },
        show:true,
        validate:false,
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let loginInfo = {
            id: this.form.id,
            pw: this.form.pw
        }
        axios.post('http://localhost:5000/user/sign-in', loginInfo).then(res => {
            console.log(res.data);
            if (res.data['result'] == 'success'){
              sessionStorage.setItem('jtw-token', res.data['access_token']);
              this.$router.push({ path: '/user/friendlist', query: { 'id': this.form.id } });
              this.validate = true;
            }
            else {
              alert("아이디와 비밀번호가 올바르지 않습니다.")
            }
            //const { accessToken } = res.data;
            }).catch(error => {
              // ... 에러 처리
              console.log(error)
            });

        //this.getList()


        // axios.post('http://localhost:5000/user/friendlist', loginInfo,  { withCredentials: true, crossorigin: true }).then(res => {
        //     console.log(res.data);
        //     }).catch(error => {
        //       // ... 에러 처리
        //       console.log(error)
        //     });
            //"http://localhost:5000/?playerinfo=";

        // var myHeaders = new Headers();
        // myHeaders.append("Authorization", `Bearer ${this.token}`);
        // fetch('http://localhost:5000/user/friendlist',{
        //     "headers":myHeaders
        // }).then(function(data){
        //     // json으로 변환된 결과를 출력합니다. 
        //     console.log("???? ");
        //     console.log(data);
        // });
        // axios.post('http://localhost:5000/user/friendlist', loginInfo).then((res) => {
        //     console.log(res.data);
        //     //"http://localhost:5000/?playerinfo=";
        // })
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.id = ''
        this.form.pw = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      signUp: function () {
        this.$router.push({ path: '/signup' });
      }
    }
  }
</script>