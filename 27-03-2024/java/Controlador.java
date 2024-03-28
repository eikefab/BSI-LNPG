
import java.util.HashMap;
import java.util.List;

public class Controlador {

    private final HashMap<Departamento, List<Empregado>> funcionarios;

    public Controlador() {
        this.funcionarios = new HashMap<>();
    }

    public HashMap<Departamento, List<Empregado>> getFuncionarios() {
        return funcionarios;
    }

    public class Empregado {

        private final int id;
        private String nome;
        private String cargo;
        private double salario;
        private Departamento departamento;

        public Empregado(int id, String nome, String cargo, double salario, Departamento departamento) {
            this.id = id;
            this.nome = nome;
            this.cargo = cargo;
            this.departamento = departamento;
        }

        public Empregado(int id, String nome, String cargo, double salario) {
            this(id, nome, cargo, salario, null);
        }

        public int getId() {
            return id;
        }
        
        public String getNome() {
            return nome;
        }

        public void setNome(String nome) {
            this.nome = nome;
        }

        public double getSalario() {
            return salario;
        }

        public void setSalario(double salario) {
            this.salario = salario;
        }

        public String getCargo() {
            return cargo;
        }

        public void setCargo(String cargo) {
            this.cargo = cargo;
        }

        public Departamento getDepartamento() {
            return departamento;
        }

        public void setDepartamento(Departamento departamento) {
            this.departamento = departamento;
        }

    }

    public class Departamento {

        private final int id;
        private final String nome;
        private final String localizacao;

        public Departamento(int id, String nome, String localizacao) {
            this.id = id;
            this.nome = nome;
            this.localizacao = localizacao;
        }

        public int getId() {
            return id;
        }

        public String getNome() {
            return nome;
        }

        public String getLocalizacao() {
            return localizacao;
        }


        public void adicionarEmpregado(Empregado empregado) {}
        public void removerEmpregado(Empregado empregado) {}

    }

}
