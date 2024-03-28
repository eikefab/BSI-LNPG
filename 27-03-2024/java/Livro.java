public class Livro {

    private final String titulo;
    private final String autor;
    private final int anoDePublicacao;
    private int copias;

    public Livro(String titulo, String autor, int anoDePublicacao, int copias) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoDePublicacao = anoDePublicacao;
        this.copias = copias;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAnoDePublicacao() {
        return anoDePublicacao;
    }

    public int getCopias() {
        return copias;
    }

    public Livro emprestar() {
        return null;
    }

    public void devolver() {
    
    }

    public boolean temCopia() {
        return false;
    }

}