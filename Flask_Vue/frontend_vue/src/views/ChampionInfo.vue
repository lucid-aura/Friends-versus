<template>
    <div class="custom-home">
        <div>
            챔피언 상세정보
        </div>
        <div>
            <div class="stat-div">
                <table class="stat-table">
                    <thead>
                        <tr>
                        <th colspan = "4" scope="cols">챔피언 스탯 정보</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th scope="row">체력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">체력 재생</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마나</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마나 재생</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">공격력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">공격 속도</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">방어력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">마법저항력</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">사거리</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                        <tr>
                        <th scope="row">이동 속도</th>
                            <td>1000</td>
                            <td>1000</td>
                            <td>1000</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="skill-div">
                <table class="skill-table">
                    <thead>
                        <tr>
                        <th colspan = "5">챔피언 스킬 정보</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                        <th  scope="row">스킬</th>
                            <td>Q</td>
                            <td>W</td>
                            <td>E</td>
                            <td>R</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'championInfo',
    created: function () {
        this.fetchDefaults();
    },
    methods: {
        clicks: function() {
            alert('clicked!')
        }
    }
}
</script>