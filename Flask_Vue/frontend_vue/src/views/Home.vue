<template>
    <div class="custom-home">
        <h1>{{ login_id }}  WELCOME!</h1>
        <form @submit.prevent="check" v-if="login_id === ''">
            <input class="custom-login-input" type="text" v-model="id" placeholder="소환사 이름을 입력해주세요." />
            <button class="custom-login-btn" type="submit">입력</button>
        </form>
        <player-info v-if="login_id !== ''" v-bind:id=this.id>
        </player-info>
    </div>
</template>

<script>
import PlayerInfo from "./PlayerInfo";
export default {
    components: {
        "player-info": PlayerInfo // 케밥 케이스로 컴포넌트 지정 https://kr.vuejs.org/v2/guide/components-props.html
    },
    data() {
        return {
            id: '',
            result: ' '
        }
    },
    props: ['login_id'],
    methods: {
        check() {
            // 소환사 이름이 제대로 입력되었는지 확인이 필요함.
            if (this.id.length === 2){ // 2글자 닉네임 시 가운데 공백이 자동으로 들어감.
                this.id = this.id[0] + ' ' + this.id[1];
            }
            if (this.id == '' ){ // 최초 로딩 시
                return false;
            }
            else if (this.id === '휘 랑'){ // player_data db에서 일치 여부 확인이 필요함. 즉 Home Vue에서 player_info DB 연동 필요
                //console.log(this.$root.$children[0]);

                //login_id = this.id
                this.$root.$children[0].$children[0].$children[1].login_id = this.id; //Base 상위 컴포넌트에 login_id 전달
                this.$root.$children[0].$children[0].$children[0].check_login = true; // NavBar sibling 컴포넌트에 로그인 정보 전달.
                this.$root.$children[0].$children[0].$children[0].user_name = this.id;

                alert(this.id + "님 반가워요!");
                return true; // 로그인 성공 시 return true하여 player_info component 보여줌
                //this.$router.push({path:'/friendlist', query: { id: this.id }})
            }
            else {
                alert("존재하지 않는 사용자 이름입니다.");
                return false;
            }
        },

    }
}
</script>