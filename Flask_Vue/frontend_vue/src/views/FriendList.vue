<template>
    <div class="custom-home">
        <main role="main" class="inner cover">
            <h3 class="cover-heading">{{ this.nickname }} 's Friend List
                <v-icon v-blur :class="icons[3].class">
                    {{ icons[3].icon }}
                </v-icon>   
                
            </h3>
            <v-layout justify-center justify-content-center mt-4>
                <v-simple-table fixed-header>
                    <template v-slot:default v-if="isLogin()">
                        <thead>
                            <th></th>
                            <th>Real Name</th>
                            <th>Lol Name</th>
                            <th>Memo</th>
                            <th style="display: none;">Missing?</th>
                            <th></th>
                            <th></th>
                        </thead>
                        <tbody v-cloak>
                            <tr v-for="(item, index) in friend_list"
                                :key="index"
                            >
                                <td>
                                    <v-icon v-blur
                                            @click="checkRow(friend_list[index])"
                                            :class="icons[0].class"
                                    >
                                        {{ icons[0].icon }}
                                    </v-icon>
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].realname"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].lolname"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].memo"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td style="display: none;">
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].missing"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <!-- <td style="display: none;"> -->
                                <td>
                                    <v-icon v-blur
                                            @click="saveRow(index)"
                                            :class="icons[4].class"
                                    >
                                        {{  icons[4].icon   }}
                                    </v-icon>
                                </td>
                                <td>
                                    <v-icon v-blur
                                            @click="removeRow(index)"
                                            :class="icons[1].class"
                                    >
                                        {{  icons[1].icon   }}
                                    </v-icon>
                                </td>
                            </tr>
                            <tr class="no-highlight">
                                <td>
                                    <v-icon v-blur
                                            @click="addRow"
                                            :class="icons[2].class"
                                    >
                                        {{  icons[2].icon   }}
                                    </v-icon>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-layout>
        </main>
        <player-info v-if="clicked_id !== ''" v-bind:id=this.clicked_id v-bind:player_info=this.player_info>
        <!-- v-bind로 자식 컴포넌트인 PlayerInfo.vue 에 player_info 값을 넘겨준다.-->
        </player-info>
    </div>
</template>

<script>
import axios from 'axios';
import PlayerInfo from "./PlayerInfo";
export default {
    name: 'friendList',
    props: ["login_id"],
    components: {
        "player-info": PlayerInfo // 케밥 케이스로 컴포넌트 지정 https://kr.vuejs.org/v2/guide/components-props.html
    },
    data() {
        return {
            user: this.login_id,
            id : '',
            nickname : '',
            token : '',
            friend_list: [],
            clicked_id: '',
            player_info: [],
            icons: [
                {
                    'icon': 'mdi-card-text-outline',
                    'class': 'v-icon-highlighted',
                    'style': '',
                },
                {
                    'icon': 'mdi-close',
                    'class': 'v-icon-highlighted',
                    'style': '' 
                },
                {
                    'icon': 'mdi-plus',
                    'class': 'v-icon-highlighted',
                    'style': '' 
                },
                {
                    'icon': 'mdi-refresh',
                    'class': 'v-icon-highlighted',
                    'style': '' 
                },
                {
                    'icon': 'mdi-content-save',
                    'class': 'v-icon-highlighted pl-1 pb-1',
                    'style': '' 
                }
            ],
            icon_list: []
        }
    },
    created: function () {
        // this.friend_list = [
        //         {
        //             'realname' : '',
        //             'lolname' : '',
        //             'memo' : '',
        //             'missing' : true
        //         },
        // ];
        this.friend_list = [];
        this.icons_list = [];
        let token = sessionStorage.getItem('jtw-token') || '';
        console.log("토큰은")
        console.log(typeof(token))
        if (token == ''){
            alert("먼저 로그인을 해주세요.")
            this.$router.push({ path: '/login' });
        }
        else {
            this.id = this.$route.query.id;
            this.nickname = this.$route.query.nickname;
            axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
            axios.post('http://localhost:5000/user/friendlist', { 'id': this.id }, { withCredentials: true, crossorigin: true }).then(res => {
                console.log("post")
                console.log(res.data);
                this.nickname = res.data[0]
                for (var i = 0; i < res.data[1].length; i++) {
                    res.data[1][i]['missing'] = true;
                    this.icons_list.push(this.icons[0]);
                    this.friend_list.push(res.data[1][i])
                    console.log(res.data[1][i]);
                }
                console.log(this.friend_list.length);
            });
        }
        
    },
    mounted: function () {   
        
    },

    methods: {
        isLogin: function () {
            console.log(this.user)
            if (this.user === this.user) // 로그인 유지 여부 확인.
                return true;
            else
                return false;
        },

        removeRow: function (index) {
            let token = sessionStorage.getItem('jtw-token') || '';
            axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
            axios.get('http://localhost:5000/user/friendlist', { 
                params: {
                    'call' : "delete",
                    'id' : this.id,
                    'lolname': this.friend_list[index]['lolname'],
                    }}, { withCredentials: true, crossorigin: true }
                ).then(res => {
                console.log("get")
                console.log(res.data)
                if (res.data == null){
                    alert("오류발생")
                }
                else {   
                    //this.friend_list = res.data
                }
            });
            this.friend_list.splice(index, 1);
            this.icons_list.splice(index, 1);
        },

        addRow: function () {
            this.friend_list.push({
                realname : '',
                lolname : '',
                memo : '',
                missing : true,
            });
            this.icons_list.push(this.icons[0]);
        },
        checkRow: function (friend) {
            this.clicked_id = ''
            let path = "http://localhost:5000/?playerinfo=";
            path += friend['lolname'];
            axios.get(path).then((res) => {
                console.log(res.data)
                if (res.data['status'] == null) {
                    this.clicked_id = friend['lolname']
                    this.player_info = res.data;
                }
                else {
                    console.log(res.data);
                    alert(res.data['status']['message'])
                }
            }).catch((error) => {
                console.error(error);
            });
        },
        saveRow: function (index) {
            let before = this.friend_list.length;
            console.log(before)
            let token = sessionStorage.getItem('jtw-token') || '';
            axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
            // axios.post('http://localhost:5000/user/friendlist', loginInfo,  { withCredentials: true, crossorigin: true }).then(res => {

            // }
            console.log("index")
            console.log(index)
            console.log(this.friend_list[index])
            axios.get('http://localhost:5000/user/friendlist', { 
                params: {
                    'call' : "insert",
                    'id' : this.id,
                    'realname': this.friend_list[index]['realname'], 
                    'lolname': this.friend_list[index]['lolname'],
                    'memo': this.friend_list[index]['memo'] 
                    }}, { withCredentials: true, crossorigin: true }
                ).then(res => {
                console.log(before)
                console.log(res.data.length)
                console.log(res.data)
                if (res.data['error'] != null){
                    // alert("값이 제대로 입력되지 않았습니다.")
                    alert(res.data['error'])
                    //this.removeRow(before-1)
                }
                else {   
                    this.friend_list = res.data
                }
            });
        }
    }
};
</script>