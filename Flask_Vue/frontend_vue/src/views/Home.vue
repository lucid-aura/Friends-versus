<template>
    <div class="custom-home">
        
        <img src="http://ddragon.leagueoflegends.com/cdn/10.24.1/img/profileicon/588.png">
        <h1>{{ id }}  WELCOME!!!!!!</h1>
        <div  v-if="id == ''">
            <input class="custom-search-input" type="text" id="playerinfo" name="playerinfo" placeholder="소환사 이름을 입력해주세요." />
            <input class="custom-search-btn" @click="getPlayerInfo" type="submit" value="입력">
        </div>

        <player-info v-if="id !== ''" v-bind:id=this.id v-bind:player_info=this.player_info>
            <!-- v-bind로 자식 컴포넌트인 PlayerInfo.vue 에 player_info 값을 넘겨준다.-->
        </player-info>
    </div>
</template>

<script>
import PlayerInfo from "./PlayerInfo";
import axios from 'axios';
export default {
    components: {
        "player-info": PlayerInfo // 케밥 케이스로 컴포넌트 지정 https://kr.vuejs.org/v2/guide/components-props.html
    },
    data() {
        return {
            id: '',
            player_info: [],
            result: ' ',
        }
    },
    mounted: function() {
        this.$root.$on('home', (text) => {
            this.id = text 
        });
    },
    methods: {
        getPlayerInfo() {
            var n = document.getElementById("playerinfo").value;
            let path = "http://localhost:5000/?playerinfo=";
            path += n;
            axios.get(path).then((res) => {
                if (res.data['status'] == null) {
                    this.player_info = res.data;
                    this.id = this.player_info['name']
                    console.log(res.data);
                }
                else {
                    console.log(res.data);
                    alert(res.data['status']['message'])
                }
            }).catch((error) => {
                console.error(error);
            });

            // let path = "http://localhost:5000/playerinfo";
            // axios.get(path, {
            //     playerInfo: '츄랑'
            // })
            // .then(function (response) {
            //     console.log(response);
            // })
            // .catch(function (error) {
            //     console.log(error);
            // });
        },
        // check() {

        //     console.log("test")
        //     let path = "http://localhost:5000/";
        //     axios.get(path).then((res) => {
        //         this.player_info = res.data;
        //     }).catch((error) => {
        //         console.error(error);
        //     });
        //     console.log(this.player_info);
            
        //     // 소환사 이름이 제대로 입력되었는지 확인이 필요함.
        //     if (this.id.length === 2){ // 2글자 닉네임 시 가운데 공백이 자동으로 들어감.
        //         this.id = this.id[0] + ' ' + this.id[1];
        //     }
        //     if (this.id == '' ){ // 최초 로딩 시
        //         return false;
        //     }
        //     else if (this.id === '휘 랑'){ // player_data db에서 일치 여부 확인이 필요함. 즉 Home Vue에서 player_info DB 연동 필요
        //         //console.log(this.$root.$children[0]);

        //         //login_id = this.id
        //         //this.$root.$children[0].$children[0].$children[1].login_id = this.id; //Base 상위 컴포넌트에 login_id 전달
        //         this.$root.$children[0].$children[0].$children[0].check_login = true; // NavBar sibling 컴포넌트에 로그인 정보 전달.
        //         this.$root.$children[0].$children[0].$children[0].user_name = this.id;

        //         alert(this.id + "님 반가워요!");
        //         return true; // 로그인 성공 시 return true하여 player_info component 보여줌
        //         //this.$router.push({path:'/friendlist', query: { id: this.id }})
        //     }
        //     else {
        //         alert("존재하지 않는 사용자 이름입니다.");
        //         return false;
        //     }
        // },
    }
}
</script>