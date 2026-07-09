<?php

use PHPUnit\Framework\TestCase;

require_once 'Koszyk.php';

class KoszykTest extends TestCase
{
    private Koszyk $koszyk;

    protected function setUp(): void
    {
        parent::setUp();
        $this->koszyk = new Koszyk();
    }

    public function testKoszykJestPustyPoUtworzeniu(): void
    {
        $this->assertEquals(0, $this->koszyk->iloscProduktow());
        $this->assertEquals(0.0, $this->koszyk->obliczSume());
    }

    public function testDodajPojedynczyProdukt(): void
    {
        $this->koszyk->dodajProdukt("Laptop", 2500.00);

        $this->assertEquals(1, $this->koszyk->iloscProduktow());
        $this->assertEquals(2500.00, $this->koszyk->obliczSume());
    }

    public function testDodajWieleProduktow(): void
    {
        $this->koszyk->dodajProdukt("Książka", 50.00);
        $this->koszyk->dodajProdukt("Długopis", 5.50);
        $this->koszyk->dodajProdukt("Zeszyt", 12.00);

        $this->assertEquals(3, $this->koszyk->iloscProduktow());
        $this->assertEquals(67.50, $this->koszyk->obliczSume());
    }

    public function testDodajProduktZZerowaCena(): void
    {
        $this->koszyk->dodajProdukt("Produkt darmowy", 0.0);

        $this->assertEquals(1, $this->koszyk->iloscProduktow());
        $this->assertEquals(0.0, $this->koszyk->obliczSume());
    }

    public function testDodajProduktyZZerowaCenaDoIstniejacych(): void
    {
        $this->koszyk->dodajProdukt("Monitor", 1200.00);
        $this->koszyk->dodajProdukt("Myszka", 0.0);
        $this->koszyk->dodajProdukt("Klawiatura", 0.0);

        $this->assertEquals(3, $this->koszyk->iloscProduktow());
        $this->assertEquals(1200.00, $this->koszyk->obliczSume());
    }

    public function testObliczSumeZDokladnosciaFloat(): void
    {
        $this->koszyk->dodajProdukt("Produkt A", 0.1);
        $this->koszyk->dodajProdukt("Produkt B", 0.2);
        $this->koszyk->dodajProdukt("Produkt C", 0.05);

        // Using assertEqualsWithDelta for float comparisons to account for potential precision issues
        $this->assertEqualsWithDelta(0.35, $this->koszyk->obliczSume(), 0.0000001);
    }
}