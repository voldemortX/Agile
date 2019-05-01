<template>
    <div>
        <!-- page -->
        <el-container width="200px">
            <el-header style="text-align: center; vertical-align:middle;font-size: 40px;height:100px">
                <el-row></el-row>
                <span>风险评估</span>

            </el-header>
            <el-main style="text-align: center; background-color:#000000">
                <el-row>
                    <el-radio-group v-model="method">
                        <el-radio :label="0">相乘法</el-radio>
                        <el-radio :label="1">矩阵法</el-radio>
                    </el-radio-group>
                </el-row>
                <el-row>
                    <el-button type="primary">提交</el-button>
                </el-row>
            </el-main>
            <el-main style="text-align: center">
                <el-tabs v-model="activeName" @tab-click.native="handleClick">
                    <el-tab-pane label="评估准备" name="first">
                        <el-divider content-position="left">评估目标</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="aim"></el-input>
                        <el-divider content-position="left">评估范围</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="range"></el-input>
                        <el-divider content-position="left">组建团队成员</el-divider>
                        <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="team"></el-input>
                    </el-tab-pane>
                    <el-tab-pane label="资产评估" name="second">
                        <div style="float:left">
                            <el-button type="add" @click.native="assetDialogVisible = true">添加</el-button>
                            <el-button type="modify">修改</el-button>
                            <el-button type="delete">删除</el-button>
                        </div>
                        <el-table :data="tableAsset" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="asset" label="资产名称" width="260">
                            </el-table-column>
                            <el-table-column prop="integrity" label="保密性" width="140">
                            </el-table-column>
                            <el-table-column prop="availability" label="可用性" width="140">
                            </el-table-column>
                            <el-table-column prop="confidentiality" label="完整性" width="140">
                            </el-table-column>
                            <el-table-column prop="rank" label="资产价值" width="140">
                            </el-table-column>
                            <el-table-column prop="details" label="描述" >
                            </el-table-column>
                        </el-table>
                    </el-tab-pane>
                    <el-tab-pane label="脆弱性评估" name="third">
                        <div style="float:left">
                            <el-button type="add" @click.native="vulDialogVisible = true">添加</el-button>
                            <el-button type="modify">修改</el-button>
                            <el-button type="delete">删除</el-button>
                        </div>
                        <el-table :data="tableVul" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="vulnerability" label="脆弱性名称" width="260"></el-table-column>
                            <el-table-column prop="rank" label="脆弱性等级" width="140"></el-table-column>
                            <el-table-column prop="va" label="资产关联" width="140"></el-table-column>
                            <el-table-column prop="details" label="描述"></el-table-column>
                        </el-table>
                    </el-tab-pane>
                    <el-tab-pane label="威胁评估" name="fourth">
                        <div style="float:left">
                            <el-button type="add" @click.native="threatDialogVisible = true">添加</el-button>
                            <el-button type="modify">修改</el-button>
                            <el-button type="delete">删除</el-button>
                        </div>
                        <el-table :data="tableThreat" border :header-cell-style="{background:'#FFFFFF'}" :cell-style="{background:'#FFFFFF'}">
                            <el-table-column prop="threat" label="威胁名称" width="260"></el-table-column>
                            <el-table-column prop="rank" label="威胁等级" width="140"></el-table-column>
                            <el-table-column prop="tv" label="威胁的脆弱性关联" width="140"></el-table-column>
                            <el-table-column prop="details" label="描述"></el-table-column>
                        </el-table>
                    </el-tab-pane>
                </el-tabs>
            </el-main>
        </el-container>

        <!-- dialogs -->
        <el-dialog title="添加资产" :visible.sync="assetDialogVisible" :modal-append-to-body="false">
            <el-form :model="formAsset">
                <el-form-item label="资产名称" :label-width="formLabelWidth">
                    <el-input v-model="formAsset.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="机密性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.confidentiality" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="完整性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.integrity" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="可用性" :label-width="formLabelWidth">
                    <el-select v-model="formAsset.availability" placeholder="请选择安全等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入资产描述" v-model="formAsset.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="assetDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click.native="formAssertClick(-1)">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="添加脆弱性" :visible.sync="vulDialogVisible" :modal-append-to-body="false">
            <el-form :model="formVul">
                <el-form-item label="脆弱性名称" :label-width="formLabelWidth">
                    <el-input v-model="formVul.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="脆弱性等级" :label-width="formLabelWidth">
                    <el-select v-model="formVul.rank" placeholder="请选择等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="关联已有资产" :label-width="formLabelWidth">
                    <el-checkbox-group v-model="formVul.va">
                        <el-checkbox v-for="i in tableAsset" :label="i.asset" :key="i.asset">{{i.asset}}</el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入脆弱性描述" v-model="formVul.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="vulDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click.native="formVulClick(-1)">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="添加威胁" :visible.sync="threatDialogVisible" :modal-append-to-body="false">
            <el-form :model="formThreat">
                <el-form-item label="威胁名称" :label-width="formLabelWidth">
                    <el-input v-model="formThreat.name" autocomplete="off" width="200px"></el-input>
                </el-form-item>
                <el-form-item label="威胁等级" :label-width="formLabelWidth">
                    <el-select v-model="formThreat.rank" placeholder="请选择等级">
                        <el-option label="很高" value=5></el-option>
                        <el-option label="高" value=4></el-option>
                        <el-option label="中" value=3></el-option>
                        <el-option label="低" value=2></el-option>
                        <el-option label="很低" value=1></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="关联已有脆弱性" :label-width="formLabelWidth">
                    <el-checkbox-group v-model="formThreat.tv">
                        <el-checkbox v-for="i in tableVul" :label="i.vulnerability" :key="i.vulnerability">{{i.vulnerability}}</el-checkbox>
                    </el-checkbox-group>
                </el-form-item>
                <el-form-item>
                    <el-input type="textarea" :rows="5" placeholder="请输入脆弱性描述" v-model="formVul.details"></el-input>
                </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="threatDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click.native="formThreatClick(-1)">确 定</el-button>
            </div>
        </el-dialog>

        <el-dialog title="评估结果" :visible.sync="resultDialogVisible" :modal-append-to-body="false">
            <div slot="footer" class="dialog-footer">
                <el-button @click.native="resultDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click.native="submitClick">确 定</el-button>
            </div>
        </el-dialog>
    </div>
</template>

<script>
    // Matrix method:
    // F[a][v] === level
    const F = [
        [1, 1, 2, 2, 3],
        [1, 1, 2, 3, 4],
        [1, 2, 3, 3, 4],
        [1, 2, 3, 3, 5],
        [2, 2, 4, 5, 5]
    ];
    // L[t][v] === level
    const L = [
        [1, 1, 2, 2, 3],
        [1, 2, 2, 3, 4],
        [1, 2, 3, 3, 4],
        [2, 2, 3, 4, 5],
        [2, 3, 4, 4, 5]
    ];
    // R[f][l] === level
    const R = [
        [1, 1, 2, 2, 3],
        [1, 2, 2, 3, 3],
        [1, 2, 3, 3, 4],
        [2, 2, 3, 4, 4],
        [2, 3, 4, 4, 5]
    ];

    const map = ['很低', '低', '中', '高', '很高'];

    export default {
        name: '_new',
        data() {
            return {
                // Page settings
                activeName: 'first',
                formLabelWidth: '120px',
                assetDialogVisible: false,
                threatDialogVisible: false,
                vulDialogVisible: false,
                resultDialogVisible: false,

                // Tab data
                aim: '',
                range: '',
                team: '',
                tableAsset: [
                    {asset: '测试资产', confidentiality: '很高', integrity: '中', availability: '很低', rank: '很高', details: 'blabla'}
                ],
                tableVul: [],
                tableThreat: [],

                // Form data
                formAsset: {
                    name: '',
                    availability: null,
                    integrity: null,
                    confidentiality: null,
                    details: ''
                },
                formThreat: {
                    name: '',
                    rank: null,
                    tv: [],
                    details: ''
                },
                formVul: {
                    name: '',
                    rank: null,
                    va: [],
                    details: ''
                },

                // System data
                systemname: 'test1',
                method: 0,
                tva_results: []

            }
        },

        methods: {
            levelMultiply(val) {
                // Can't have any malicious values at this point
                return Math.ceil((val - 1) / 5);
            },

            messageBox(title, text) {
                this.$alert(text, title, {
                    confirmButtonText: '确定'
                });
            },

            handleClick(tab, event) {
                console.log(tab, event);
            },

            formAssertClick(index) {
                if(this.formAsset.name === '' || this.formAsset.confidentiality === null
                    || this.formAsset.integrity === null || this.formAsset.availability === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else {
                    // Calculate val
                    let val = this.formAsset.availability;
                    if (this.formAsset.integrity > val)
                        val = this.formAsset.integrity;
                    if (this.formAsset.confidentiality > val)
                        val = this.formAsset.confidentiality;

                    // Move data
                    let temp = {
                        asset: this.formAsset.name,
                        confidentiality: map[this.formAsset.confidentiality - 1],
                        integrity: map[this.formAsset.integrity - 1],
                        availability: map[this.formAsset.availability - 1],
                        rank: map[val - 1]
                    };

                    if (index !== -1)  // Modify
                        this.tableAsset[index] = temp;
                    else  // Add
                    {
                        // Check
                        for(let i of this.tableAsset)
                            if(i.asset === temp.asset)
                            {
                                this.messageBox('错误提示', '资产已存在！');
                                return;
                            }

                        this.tableAsset.push(temp);
                    }

                    // Close dialog
                    this.formAsset = {
                        name: '',
                        availability: null,
                        integrity: null,
                        confidentiality: null
                    };
                    this.assetDialogVisible = false;
                }
            },

            formThreatClick(index) {
                if(this.formThreat.name === '' || this.formThreat.rank === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else
                {
                    // Move data
                    let temp = {
                        threat: this.formThreat.name,
                        tv: this.formThreat.tv.toString(),
                        details: this.formThreat.details,
                        rank: map[this.formThreat.rank - 1]
                    };

                    if (index !== -1)  // Modify
                        this.tableThreat[index] = temp;
                    else  // Add
                    {
                        // Check
                        for(let i of this.tableThreat)
                            if(i.threat === temp.threat)
                            {
                                this.messageBox('错误提示', '脆弱性已存在！');
                                return;
                            }

                        this.tableThreat.push(temp);
                    }

                    // Close dialog
                    this.formThreat = {
                        name: '',
                        rank: null,
                        va: [],
                        details: ''
                    };
                    this.threatDialogVisible = false;
                }
            },

            formVulClick(index) {
                if(this.formVul.name === '' || this.formVul.rank === null)
                    this.messageBox('错误提示', '请完整填写必要信息！');
                else
                {
                    // Move data
                    let temp = {
                        vulnerability: this.formVul.name,
                        va: this.formVul.va.toString(),
                        details: this.formVul.details,
                        rank: map[this.formVul.rank - 1]
                    };

                    if (index !== -1)  // Modify
                        this.tableVul[index] = temp;
                    else  // Add
                    {
                        // Check
                        for(let i of this.tableVul)
                            if(i.vulnerability === temp.vulnerability)
                            {
                                this.messageBox('错误提示', '脆弱性已存在！');
                                return;
                            }

                        this.tableVul.push(temp);
                    }

                    // Close dialog
                    this.formVul = {
                        name: '',
                        rank: null,
                        va: [],
                        details: ''
                    };
                    this.vulDialogVisible = false;
                }
            },

            calcClick() {
                // Calculate results
                // Expand from v
                for(let v of this.tableVul)
                {
                    // Search t
                    for(let t of this.tableThreat)
                    {
                        let flag = false;
                        for(let i of t.tv)
                            if(i === v.vulnerability)
                            {
                                flag = true;
                                break;
                            }

                        if(flag === true)
                        {
                            // Search a
                            for(let a of this.tableAsset)
                            {
                                flag = false;
                                for(let i of v.va)
                                    if(i === a.asset)
                                    {
                                        flag = true;
                                        break;
                                    }

                                if(flag === true)
                                {
                                    // append
                                    let temp = {asset: a.asset, vulnerability: v.vulnerability, threat: t.threat,
                                        level: 0};
                                    if(this.method === 0)  // Multiply
                                    {
                                        let val = Math.sqrt(map.indexOf(a.rank) * map.indexOf(v.rank)) *
                                            Math.sqrt(map.indexOf(v.rank) * map.indexOf(t.rank));
                                        temp.level = this.levelMultiply(val);
                                    }
                                    else  // Matrix
                                        temp.level = R[F[map.indexOf(a.rank)][map.indexOf(v.rank)]][L[map.indexOf(t.rank)][map.indexOf(v.rank)]];

                                    this.tva_results.push(temp);
                                }
                            }
                        }
                    }
                }

                // Show results
            },

            submitClick() {
                // Submit a system to server
            },
        }
    };
</script>


<style scoped>
    .el-button{
        width:74px;
        height:40px;
        font-size:17px;
    }
</style>
<style>
    .el-header {
        background-color: #000000;
        color: #FFFFFF;
        line-height: 70px;
    }
    .el-main {
        background-color:#FFFFFF;
    }
</style>
