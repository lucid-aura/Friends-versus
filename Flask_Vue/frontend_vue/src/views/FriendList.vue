<template>
    <div class="custom-home">
        <main role="main" class="inner cover">
            <h3 class="cover-heading">{{ this.nickname }} 's Friend List
                <v-icon v-blur :class="icons[4].class">
                    {{ icons[4].icon }}
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
                                            :class="icons_list[index].class"
                                            @click="checkRow(index)"
                                            v-model="icons_list[index]"
                                    >
                                        {{ icons_list[index].icon }}
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
                                    >
                                        {{  icons[5].icon   }}
                                    </v-icon>
                                </td>
                                <td>
                                    <v-icon v-blur
                                            @click="removeRow(index)"
                                    >
                                        {{  icons[2].icon   }}
                                    </v-icon>
                                </td>
                            </tr>
                            <tr class="no-highlight">
                                <td>
                                    <v-icon v-blur
                                            @click="addRow"
                                            :class="icons[3].class"
                                    >
                                        {{  icons[3].icon   }}
                                    </v-icon>
                                </td>
                            </tr>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-layout>
        </main>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'friendList',
    props: ["login_id"],
    data() {
        return {
            user: this.login_id,
            id : '',
            nickname : '',
            token : '',
            friend_list: [],
            icons: [
                {
                    'icon': 'mdi-checkbox-blank-outline',
                    'class': '',
                    'style': 'text-decoration:none;color:unset;' 
                },
                {
                    'icon': 'mdi-checkbox-mark-outline',
                    'class': 'v-icon-highlighted',
                    'style': 'text-decoration:line-through;color:#adb7bbd1;' 
                },
                {
                    'icon': 'mdi-close',
                    'class': '',
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
        checkRow: function (index) {
            if (this.icons_list[index].icon == this.icons[0].icon) {
                this.icons_list[index] = this.icons[1];
                this.friend_list[index].missing = false;
            } else {
                this.icons_list[index] = this.icons[0];
                this.friend_list[index].missing = true;
            }
        },
        saveRow: function (index) {
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
                console.log("get")
                console.log(res.data)
                if (res.data == null){
                    alert("오류발생")
                }
                else {   
                    //this.friend_list = res.data
                }
            });
        }
    }
};
</script>