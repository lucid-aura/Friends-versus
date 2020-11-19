<template>
    <div class="custom-home">
        <h1>{{ login_id }}  WELCOME!</h1>
        <form @submit.prevent="check">
            <input class="custom-login-input" type="text" v-model="id" placeholder="소환사 이름을 입력해주세요." />
            <button class="custom-login-btn" type="submit">입력</button>
        </form>
    </div>
</template>

<script>

export default {
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

            if (this.id == '' || this.id == ' '){
                alert('제대로 된 입력을 해주세요.');
                console.log(this.$root.$children[0].$children[0].check_login);
            }
            else {
                console.log(this.$root.$children[0].$children[1]);

                this.$root.$children[0].$children[1].login_id = this.id;

                this.$root.$children[0].$children[0].check_login = true;
                this.$root.$children[0].$children[0].user_name = this.id;

                alert(this.id + "님 반가워요!");
                //this.$router.push({path:'/friendlist', query: { id: this.id }})
            }
        },

    }
}
</script>