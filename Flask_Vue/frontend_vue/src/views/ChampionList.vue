<template>
    <div class="custom-home">
        <main role="main" class="inner cover">
            <h3 class="cover-heading">
                Champion
            </h3>
            <v-layout justify-center justify-content-center mt-4>
                <v-simple-table fixed-header height="300px">
                    <template v-slot:default>
                        <thead>
                            <th>Champion Icon</th>
                            <th>Champion Name</th>
                            <th>Champion Title</th>
                        </thead>
                        <tbody v-cloak>
                            <tr @click="select(item['id'])" v-for="(item, index) in champion_list"
                                :key="index"
                            >
                                <td>
                                    <img :src=getChampionIcon(index) />
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="item['name']"
                                            readonly=true
                                    />
                                    <router-link to="/championinfo"></router-link>
                                    <router-view></router-view>
                                </td>
                                <td>
                                    <input  class="on-fly-input"
                                            v-model="item['title']"
                                            readonly=true
                                    />
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
import axios from 'axios';
export default {
    name: 'championList',
    data() {
        return {
            selected_champion: '',
            champion_list: [],
            icon_url: ""
        }
    },
    mounted() {
        let path = "http://localhost:5000/championlist";
        axios.post(path).then((res) => {
            var results = JSON.parse(res.data);
            this.champion_list = results;
        }).catch((error) => {
            console.error(error);
        });
        
    },
    methods: {
        getChampionIcon(index) {
            var path = 'http://ddragon.leagueoflegends.com/cdn/10.24.1/img/champion/';
            path += this.champion_list[index]['id'];
            path += '.png';
            this.url = path;
            return path;
        },
        /*
        fetchDefaults: function () {

            this.champion_list = [
                {
                    'champion_name' : '조이',
                    'champion_title' : '여명의 성위',
                    'missing' : true
                },
                {
                    'champion_name' : '챔피언 이름',
                    'champion_title' : '챔피언 타이틀',
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
        */

        select(id) {
            this.$router.push({path:'/championinfo',query:{championinfo: id} }); // 쿼리로 챔피언 이름을 넘겨준다.
        }
    }
}
</script>