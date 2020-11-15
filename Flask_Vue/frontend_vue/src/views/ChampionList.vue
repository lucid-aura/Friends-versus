<template>
    <div class="custom-home">
        <main role="main" class="inner cover">
            <h3 class="cover-heading">Champion
                <v-icon v-blur @click="fetchDefaults" :class="icons[4].class">
                    {{ icons[4].icon }}
                </v-icon>   
            </h3>
            <v-layout justify-center justify-content-center mt-4>
                <v-simple-table fixed-header>
                    <template v-slot:default>
                        <thead>
                            <th></th>
                            <th>Champion Name</th>
                            <th>Champion Title</th>
                            <th style="display: none;">Missing?</th>
                            <th></th>
                        </thead>
                        <tbody v-cloak>
                            <tr v-for="(item, index) in champion_list"
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
                                            v-model="champion_list[index].champion_name"
                                            :style="icons_list[index].style"
                                            @click.left="wow"
                                    />
                                    <router-link to="/championinfo"></router-link>
                                    <router-view></router-view>
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="champion_list[index].champion_title"
                                            :style="icons_list[index].style"
                                    />
                                </td>
                                <td style="display: none;">
                                    <input  class="on-fly-input"
                                            v-model="champion_list[index].missing"
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
                            <router-link to="/championinfo"></router-link>
                            <router-view></router-view>
                        </tbody>
                    </template>
                </v-simple-table>
            </v-layout>
        </main>
    </div>
</template>

<script>
export default {
    name: 'championList',
    data() {
        return {
            champion_list: [],
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
        fetchDefaults: function () {

            this.champion_list = [
                {
                    'champion_name' : '아트록스',
                    'champion_title' : '다르킨의 검',
                    'missing' : true
                },
                {
                    'champion_name' : '조이',
                    'champion_title' : '여명의 성위',
                    'missing' : true 
                }
            ];

            this.icons_list = [];
            for (var i = 0; i < this.champion_list.length; i++) {
                if (this.champion_list[i].missing == true) {
                    this.icons_list.push(this.icons[0]);
                } else {
                    this.icons_list.push(this.icons[1]);
                }
            }
        },

        removeRow: function (index) {
            this.champion_list.splice(index, 1);
            this.icons_list.splice(index, 1);
        },

        addRow: function () {
            this.champion_list.push({
                champion_name : '',
                champion_title : '',
                missing : true,
            });
            this.icons_list.push(this.icons[0]);
        },
        checkRow: function (index) {
            if (this.icons_list[index].icon == this.icons[0].icon) {
                this.icons_list[index] = this.icons[1];
                this.champion_list[index].missing = false;
            } else {
                this.icons_list[index] = this.icons[0];
                this.champion_list[index].missing = true;
            }
        },

        directives: {
            focus: {
                inserted (el) {
                    el.focus();
                }
            }
        },

        wow: function() {
            this.$router.push('/championinfo')
        }
    }
}
</script>