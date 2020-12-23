<template>
  <div class="custom-home">
    <form @submit="onSubmit" @reset="onReset" v-if="show">
        <input class="custom-login-input" id="id" name="id" v-model="form.id" placeholder="id"/>
        <input class="custom-login-input" type='password' id="pw" name="pw" v-model="form.pw" placeholder="pw"/>
        <input class="custom-login-btn" type='submit' value='login' />
    </form>
  </div>
</template>

<script>
//import PlayerInfo from "./PlayerInfo";
import axios from 'axios';
  export default {
    data() {
      return {
        form: {
          id: '',
          pw: '',
        },
        show:true,
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let loginInfo = {
            id: this.form.id,
            pw: this.form.pw
        }
        axios.post('http://localhost:5000/user/sign-in', loginInfo).then((response) => {
            console.log(response.data);
            //"http://localhost:5000/?playerinfo=";
        })
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
      login: function () {
        let loginInfo = {
            id: this.form.username,
            pw: this.form.password
        }
        this.axios.post('/user/sign-in', loginInfo).then((response) => {
            console.log(response.data);
            //"http://localhost:5000/?playerinfo=";
        })
      }
    }
  }
</script>