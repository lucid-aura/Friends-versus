<template>
    <div class="custom-home">
        <form @submit="onSubmit" @reset="onReset" v-if="show">
            <div>
                <input class="custom-login-input" id="id" name="id" v-model="form.id" placeholder="id"/>
                <button class="custom-method-btn" type='button' @click="idCheck"> check </button>
            </div>
            <div>
                <input class="custom-login-input" type='password' @input="pwCheck" id="pw" name="pw" v-model="form.pw" placeholder="pw"/>
                <span class="custom-method-btn" id="checkpw" name="checkpw" style="width:70px">{{ this.pwcheck }} </span>
            </div>
            <div>
                <input class="custom-login-input" id="lolname" name="lolname" v-model="form.lolname" placeholder="lolname"/>
                <button class="custom-method-btn" type='button' @click="lolnameCheck"> check </button>
            </div>
            <div>
                <input class="custom-login-input" id="nickname" name="nickname" v-model="form.nickname" placeholder="nickname"/>
                <button class="custom-method-btn" type='button' @click="nicknameCheck"> check </button>
            </div>
            <div>
                <input class="custom-login-btn" type='reset' value='reset'/>
                <input class="custom-method-btn" type='submit' value='signup'/>
                
            </div>
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
            pwcheck:'8자리이상',
            show:true,
            validate:false,
        }
        },
        methods: {
        onSubmit(event) {
            event.preventDefault()
            if (this.pwcheck != 'Able') {
                alert("불가능한 비밀번호 입니다.")
            }
            else{
                let signupInfo = {
                    check: 'submit',
                    id: this.form.id,
                    pw: this.form.pw,
                    lolname: this.form.lolname,
                    nickname: this.form.nickname
                }
                axios.post('http://localhost:5000/user/sign-up', signupInfo).then(res => {
                    console.log(res.data);
                    if (res.data['result'] == 'success'){
                        this.$router.push({ path: '/login' });
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
            }
            
        },
        onReset(event) {
            event.preventDefault()
            // Reset our form values
            this.form.id = ''
            this.form.pw = ''
            this.form.lolname = ''
            this.form.nickname = ''
            // Trick to reset/clear native browser form validation state
            this.show = false
            this.$nextTick(() => {
                this.show = true
            })
        },
        idCheck() {
            let signupInfo = {
                check: 'id',
                id: this.form.id
            }
            axios.post('http://localhost:5000/user/sign-up', signupInfo).then(res => {
                console.log(res.data);
                if (res.data['result'] == 'success'){
                    alert("사용 가능한 ID입니다.")
                }
                else {
                    alert("사용 불가능한 ID입니다.")
                }
                //const { accessToken } = res.data;
                }).catch(error => {
                // ... 에러 처리
                console.log(error)
            });
            // alert(this.form.id)
        },
        pwCheck() {
            if (this.form.pw.length >= 8){
                this.pwcheck = 'Able'
            }
            else {
                this.pwcheck = 'Unable'
            }
        },
        nicknameCheck() {
            let signupInfo = {
                check: 'nickname',
                nickname: this.form.nickname
            }
             axios.post('http://localhost:5000/user/sign-up', signupInfo).then(res => {
                console.log(res.data);
                if (res.data['result'] == 'success'){
                    alert("사용 가능한 닉네임입니다.")
                }
                else {
                    alert("사용 불가능한 닉네임입니다.")
                }
                //const { accessToken } = res.data;
                }).catch(error => {
                // ... 에러 처리
                console.log(error)
            });
        },
        lolnameCheck() {
            let signupInfo = {
                check: 'lolname',
                lolname: this.form.lolname
            }
            axios.post('http://localhost:5000/user/sign-up', signupInfo).then(res => {
                console.log(res.data);
                if (res.data['result'] == 'success'){
                    alert("인증 가능한 롤네임입니다.")
                }
                else {
                    alert("이미 등록된 롤네임입니다.")
                }
                //const { accessToken } = res.data;
                }).catch(error => {
                // ... 에러 처리
                console.log(error)
            });
        },
        }
    }
</script>