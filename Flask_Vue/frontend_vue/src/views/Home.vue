<template>
    <div class="custom-home">
        <form @submit.prevent="check">
            <input class="custom-login-input" type="text" v-model="id" placeholder="소환사 이름을 입력해주세요." />
            <button class="custom-login-btn" type="submit">입력</button>
            <p v-bind:id="result">{{result}}</p>
        </form>
        <Base />
    </div>
</template>

<script>
import Base from '@/components/Base.vue'

export default {
    name: 'home',
    data() {
        return {
            id: '',
            result: ' '
        }
    },
    components: {
        Base
    },
    methods: {
        check() {
            // 소환사 이름이 제대로 입력되었는지 확인이 필요함.
            /*
            if (this.id == '' || this.id == ' '){
                this.result = this.id
                alert('제대로 된 입력을 해주세요.')
            }
            else {
                alert('아이디 검색')
            }
            */
            alert('a')
            this.$router.push("/friendlist")

        }
    }
}
</script>