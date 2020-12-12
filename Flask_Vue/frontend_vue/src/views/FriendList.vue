<template>
    <div class="custom-home">
        <main role="main" class="inner cover">
            <h3 class="cover-heading">{{ this.user }} 's Friend List
                <v-icon v-blur @click="fetchDefaults" :class="icons[4].class">
                    {{ icons[4].icon }}
                </v-icon>   
                
            </h3>
            <v-layout justify-center justify-content-center mt-4>
                <v-simple-table fixed-header>
                    <template v-slot:default v-if="isLogin()">
                        <thead>
                            <th></th>
                            <th>Real Name</th>
                            <th>Nick Name</th>
                            <th style="display: none;">Missing?</th>
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
                                            v-model="friend_list[index].real_name"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].nick_name"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td style="display: none;">
                                    <input  class="on-fly-input"
                                            v-model="friend_list[index].missing"
                                            :style="icons_list[index].style"
                                    />
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
export default {
    name: 'friendList',
    props: ["login_id"],
    data() {
        return {
            user: this.login_id,
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
                    'class': 'v-icon-highlighted pl-1 pb-1',
                    'style': '' 
                }
            ],
            icon_list: []
        }
    },
    created: function () {
        this.fetchDefaults();
    },

    methods: {
        isLogin: function () {
            console.log(this.user)
            if (this.user === this.user) // 로그인 유지 여부 확인.
                return true;
            else
                return false;
        },
        fetchDefaults: function () { // Player_friends 친구 db에 list를 가지고 와야함.
            this.friend_list = [
                {
                    'real_name' : '현상현',
                    'nick_name' : '휘랑',
                    'missing' : true
                },
                {
                    'real_name' : '안상원',
                    'nick_name' : '피곤한통닭',
                    'missing' : true 
                }
            ];

            this.icons_list = [];
            for (var i = 0; i < this.friend_list.length; i++) {
                if (this.friend_list[i].missing == true) {
                    this.icons_list.push(this.icons[0]);
                } else {
                    this.icons_list.push(this.icons[1]);
                }
            }
        },

        removeRow: function (index) {
            this.friend_list.splice(index, 1);
            this.icons_list.splice(index, 1);
        },

        addRow: function () {
            this.friend_list.push({
                real_name : '',
                nick_name : '',
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
    }
};
</script>